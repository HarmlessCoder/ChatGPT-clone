/** @type {import('tailwindcss').Config} */
module.exports = {
  content: ["./templates/*.html"],
  theme: {
    extend: {

      colors:{
        // chatblack: 'rgba(52,53,65,var(--tw-bg-opacity))',
        chatblack: {50:'#343541'}
      }
    },
  },
  plugins: [],
}

