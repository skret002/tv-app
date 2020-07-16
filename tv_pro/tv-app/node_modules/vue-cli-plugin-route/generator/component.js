const fs = require('fs');
const recast = require('recast');

// eslint-disable-next-line no-unused-vars
module.exports = (api, options, rootOptions) => {
  if (fs.existsSync(`src/components/${options.name}.vue`)) {
    // eslint-disable-next-line no-console
    console.warn(`\nComponent ${options.name} already exists`);
    return;
  }

  api.injectImports('src/router/index.js', `import ${options.name} from '../components/${options.name}.vue'`);

  api.render({
    [`src/components/${options.name}.vue`]: 'template/component/index.vue',
  });

  api.postProcessFiles((files) => {
    const ast = recast.parse(files['src/router/index.js']);
    const expression = `({\n  path: '${options.route}',\n  name: '${options.name}',\n  component: ${options.name}\n})`;
    const objectExpression = recast.parse(expression).program.body[0].expression;

    recast.types.visit(ast, {
      visitVariableDeclarator({ node }) {
        if (node.id.name === 'routes' && node.init.type === 'ArrayExpression') {
          node.init.elements.push(objectExpression);
        }

        return false;
      },
    });

    // eslint-disable-next-line no-param-reassign
    files['src/router/index.js'] = recast.print(ast).code;
  });
};
