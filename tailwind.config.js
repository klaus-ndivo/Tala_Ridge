// tailwind.config.js
module.exports = {
  darkMode: 'class', // 👈 Add this line
  content: [
    './templates/**/*.{html,js}', // adjust paths to your files
    './static/**/*.{html,js}',
  ],
  theme: {
    extend: {},
  },
  plugins: [],
}
