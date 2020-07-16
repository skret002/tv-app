module.exports = [
  {
    name: 'type',
    type: 'list',
    message: 'What do you want to generate?',
    choices: [
      {
        name: 'Initial framework',
        value: 'init',
      },
      {
        name: 'Route with component',
        value: 'component',
      },
    ],
  },
  {
    when: answers => answers.type === 'init',
    name: 'history',
    type: 'confirm',
    message: 'Use history mode for router?',
  },
  {
    when: answers => answers.type === 'component',
    name: 'name',
    type: 'input',
    message: 'Name of the component?',
    validate: input => (input !== '' ? true : 'Name is required.'),
  },
  {
    when: answers => answers.type === 'component',
    name: 'route',
    type: 'input',
    message: 'Route of the component?',
    validate: input => (input !== '' ? true : 'Route is required.'),
  },
];
