/** @type {import('tailwindcss').Config} */
module.exports = {
  content: ["./templates/*.html"],
  theme: {
    fontFamily: {
      'Iter': ['Iter', 'sans-serif'],
    },
    extend: {
      colors: {
        'poke-dark-grey': '#E6E6E6',
      }
    },
  },
  plugins: [],
}

