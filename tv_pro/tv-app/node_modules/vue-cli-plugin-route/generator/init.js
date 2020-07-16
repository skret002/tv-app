// eslint-disable-next-line no-unused-vars
module.exports = (api, options, rootOptions) => {
  api.injectImports(api.entryFile, 'import router from \'./router\'');
  api.injectRootOptions(api.entryFile, 'router');

  api.extendPackage({
    dependencies: {
      'vue-router': '^3.0.1',
    },
  });

  api.render('./template/init', {
    history: options.history,
  });
};
