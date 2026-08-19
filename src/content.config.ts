import { defineCollection, z } from 'astro:content';
import { glob } from 'astro/loaders';

const posts = defineCollection({
  loader: glob({ pattern: '**/*.{md,mdx}', base: './src/content/posts' }),
  schema: z.object({
    title: z.string(),
    description: z.string(),
    date: z.coerce.date(),
    updated: z.coerce.date().optional(),
    tags: z.array(z.string()).optional(),
    category: z.string().optional(),
    author: z.string().optional(),
    image: z.object({ url: z.string(), alt: z.string(), position: z.string().optional() }).optional(),
    draft: z.boolean().optional().default(false),
    audioUrl: z.string().optional(),
    substackUrl: z.string().url().optional(),
  }),
});

export const collections = { posts };
