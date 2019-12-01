const AWS = require('aws-sdk');

AWS.config.update({
    region: 'us-west-2'
});

const S3 = new AWS.S3();

exports.handler = async event => {
    // TODO implement
    console.log(event);
    return S3.getSignedUrlPromise('getObject', {
        Bucket: 'virtual-tour-storage',
        Key: 't-from-t-mobile-logo-386329.png'
    })
        .then(result => {
            console.log(result);
            const response = {
                statusCode: 200,
                body: {
                    signedUrl: result
                }
            };
            return response;
        })
        .catch(error => {
            const response = {
                statusCode: 500,
                body: error
            };
            return response;
        });
};
