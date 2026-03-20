import { defineCollection, z } from 'astro:content';

const posts = defineCollection({
  type: 'content',
  schema: z.object({
    title: z.string(),
    description: z.string(),
    date: z.coerce.date(),
    tags: z.array(z.string()).optional(),
    author: z.string().optional(),
    image: z.object({ url: z.string(), alt: z.string() }).optional(),
    draft: z.boolean().optional().default(false),
    audioUrl: z.string().optional(),
  }),
});

export const collections = { posts };
