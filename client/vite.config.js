import { fileURLToPath, URL } from 'node:url';

import { defineConfig } from 'vite';
import vue from '@vitejs/plugin-vue';
import svgLoader from 'vite-svg-loader';

// https://vitejs.dev/config/
export default defineConfig({
  plugins: [
    vue(),
    svgLoader(),
  ],
  resolve: {
    alias: {
      '@': fileURLToPath(new URL('./src', import.meta.url)),
    }
  },
  css: {
    preprocessorOptions: {
      scss: {
        additionalData: `
          @import "@/assets/scss/_config.scss";
          @import "@/assets/scss/base/_reset.scss";
          @import "@/assets/scss/base/_generic.scss";
          @import "@/assets/scss/utils/_functions.scss";
          @import "@/assets/scss/utils/_mixins.scss";
        `,
      },
    },
  },
});
