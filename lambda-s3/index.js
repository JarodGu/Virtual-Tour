// const AWS = require('aws-sdk');

// AWS.config.update({
//     region: 'us-west-2'
// });

// const S3 = new AWS.S3();

exports.handler = async event => {
    // TODO implement
    console.log(event);
    // S3.getSignedUrlPromise('getObject', {
    //     Bucket: 'bucket',
    //     Key: 'key'
    // })
    const response = {
        statusCode: 200,
        body: JSON.stringify(event)
    };
    return response;
};
