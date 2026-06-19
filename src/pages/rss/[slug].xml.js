import rss from '@astrojs/rss';
import { getCollection } from 'astro:content';
import MarkdownIt from 'markdown-it';
import sanitizeHtml from 'sanitize-html';

const parser = new MarkdownIt();

export async function getStaticPaths() {
  const posts = await getCollection('posts', ({ data }) => !data.draft);
  return posts.map((post) => ({ params: { slug: post.id.replace(/\.mdx?$/, '') } }));
}

export async function GET(context) {
  const posts = await getCollection('posts');
  const post = posts.find((p) => p.id.replace(/\.mdx?$/, '') === context.params.slug);

  return rss({
    title: `Chukwuma Theology — ${post.data.title}`,
    description: post.data.description,
    site: context.site,
    items: [
      {
        title: post.data.title,
        pubDate: post.data.date,
        description: post.data.description,
        link: `/posts/${post.id.replace(/\.mdx?$/, '')}/`,
        content: sanitizeHtml(parser.render(post.body), {
          allowedTags: sanitizeHtml.defaults.allowedTags.concat(['img']),
          allowedAttributes: {
            ...sanitizeHtml.defaults.allowedAttributes,
            img: ['src', 'alt'],
          },
        }),
      },
    ],
    customData: `<language>en-us</language>`,
  });
}
