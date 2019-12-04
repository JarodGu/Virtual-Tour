const express = require('express');
const app = express();

const history = require('connect-history-api-fallback');

const port = process.env.PORT || 3000;

app.use(history());
app.use(express.static('./dist'));

app.listen(port, () => {
    console.log('listening on port ' + port);
});
