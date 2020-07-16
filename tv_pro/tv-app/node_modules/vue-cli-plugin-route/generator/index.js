const prettier = require('prettier');

module.exports = (api, options, rootOptions) => {
  // TODO: Typescript support
  // TODO: Post process lint

  // eslint-disable-next-line global-require, import/no-dynamic-require
  require(`./${options.type}`)(api, options, rootOptions);

  api.postProcessFiles((files) => {
    // eslint-disable-next-line no-param-reassign
    files['src/router/index.js'] = prettier.format(files['src/router/index.js'], {
      semi: false,
      singleQuote: true,
      parser: 'babylon',
    });
  });
};
