import { defineConfig } from 'astro/config';
import mdx from '@astrojs/mdx';
import sitemap from '@astrojs/sitemap';

export default defineConfig({
  site: 'https://chukwumaonyeije.github.io',
  base: '/chukwuma-theology',
  integrations: [mdx(), sitemap()],
});
