import { defineConfig } from 'astro/config';
import mdx from '@astrojs/mdx';

export default defineConfig({
  site: 'https://chukwumaonyeije.github.io',
  base: '/chukwuma-theology',
  integrations: [mdx()],
});
