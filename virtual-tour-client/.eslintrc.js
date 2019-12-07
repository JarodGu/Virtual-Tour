module.exports = {
    root: true,

    env: {
        node: true
    },

    extends: ['plugin:vue/essential'],

    rules: {
        'vue/no-unused-vars': 'warning'
    },

    parserOptions: {
        parser: 'babel-eslint'
    }

    // extends: ['plugin:vue/essential', 'eslint:recommended']
};
