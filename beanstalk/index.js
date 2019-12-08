const express = require('express');
const app = express();
const history = require('connect-history-api-fallback');
const cors = require('cors');
const expressFormidable = require('express-formidable');
const fs = require('fs');
const AWS = require('aws-sdk');
const lambda = new AWS.Lambda({
    region: 'us-west-2'
});

const port = process.env.PORT || 3000;
app.use(cors());
app.use(expressFormidable());

app.get('/api/image', (request, response) => {
    const params = {
        FunctionName: 'GetImageInfo',
        InvocationType: 'RequestResponse',
        Payload: JSON.stringify({
            ImageID: Number.parseInt(request.query.ImageID),
            AlbumID: Number.parseInt(request.query.AlbumID)
        })
    };

    lambda
        .invoke(params)
        .promise()
        .then(result => {
            response.send(JSON.parse(JSON.parse(result.Payload).body));
        })
        .catch(error => {
            response.send(error);
        });
});

app.post('/api/album', cors(), (request, response) => {
    const S3 = new AWS.S3({
        region: 'us-west-2'
    });
    console.log(request.fields);
    const fileName = request.files.file.name,
        albumName = request.fields.albumName;
    console.log(fileName, albumName);

    fs.readFile(request.files.file.path, async (err, data) => {
        try {
            console.log(data);

            const params = {
                Body: data,
                Bucket: 'virtual-tour-storage',
                Key: `${albumName}/${fileName}`
            };

            console.log(params);

            const result = await S3.putObject(params).promise();

            const createParams = {
                FunctionName: 'CreateImageItem',
                InvocationType: 'RequestResponse',
                Payload: JSON.stringify({
                    AlbumName: albumName,
                    AlbumDescription: 'This is a new album',
                    S3URL: `https://virtual-tour-storage.s3-us-west-2.amazonaws.com/${albumName}/${fileName}`,
                    Annotations: [],
                    Location: 'Seattle'
                })
            };

            const result2 = await lambda.invoke(createParams).promise();
            console.log(result2);
            response.send({ info: 'request finished' });
        } catch (error) {
            console.log(error);
            response.send(error);
        }
    });
});

app.get('/api/album', async (request, response) => {
    console.log(request.query);

    const params = {
        FunctionName: 'GetAlbumImages',
        InvocationType: 'RequestResponse',
        Payload: JSON.stringify({
            AlbumID: Number.parseInt(request.query.id)
        })
    };
    console.log(params);

    let result = await lambda.invoke(params).promise();
    const albumImages = JSON.parse(JSON.parse(result.Payload).body);

    const params1 = {
        FunctionName: 'GetAlbumInfo',
        InvocationType: 'RequestResponse',
        Payload: JSON.stringify({
            AlbumID: Number.parseInt(request.query.id)
        })
    };

    result = await lambda.invoke(params1).promise();
    const albumInfo = JSON.parse(JSON.parse(result.Payload).body);

    response.send({
        images: albumImages,
        ...albumInfo
    });
});

app.get('/api/albums', (request, response) => {
    const params = {
        FunctionName: 'GetAlbumsList',
        InvocationType: 'RequestResponse'
    };

    lambda
        .invoke(params)
        .promise()
        .then(result => {
            response.send(JSON.parse(JSON.parse(result.Payload).body));
        })
        .catch(error => {
            response.send(error);
        });
});

app.use(history());
app.use(express.static('./dist'));

app.listen(port, () => {
    console.log('listening on port ' + port);
});
