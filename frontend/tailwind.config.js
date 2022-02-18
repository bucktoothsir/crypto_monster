module.exports = {
  content: ["./index.html"],
  theme: {
    fontSize: {
      'xxs': '.55rem',
    },
  },
  variants: {
    outline: ["focus"],
  },
  plugins: [
    require('flowbite/plugin')
]
}