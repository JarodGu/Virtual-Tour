const express = require('express');
const app = express();
const history = require('connect-history-api-fallback');
const AWS = require('aws-sdk');
const lambda = new AWS.Lambda({
    region: 'us-west-2'
});

const port = process.env.PORT || 3000;

app.get('/api/album', (request, response) => {
    const params = {
        FunctionName: 'GetAlbumImages',
        InvocationType: 'RequestResponse',
        Payload: JSON.stringify({
            AlbumID: 3
        })
    };

    lambda
        .invoke(params)
        .promise()
        .then(result => {
            response.send(result);
        })
        .catch(error => {
            response.send(error);
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
            response.send(result);
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
