import MarkdownIt from 'markdown-it'
import anchorPlugin from 'markdown-it-anchor'
import attrsPlugin from 'markdown-it-attrs'
// @ts-ignore
import { full as emojiPlugin } from 'markdown-it-emoji'
import type {
  BuiltinTheme,
  Highlighter,
  LanguageInput,
  ShikiTransformer,
  ThemeRegistrationAny
} from 'shiki'
import type { Logger } from 'vite'
import { containerPlugin, type ContainerOptions } from './plugins/containers'
import { highlight } from './plugins/highlight'
import { highlightLinePlugin } from './plugins/highlightLines'
import { imagePlugin, type Options as ImageOptions } from './plugins/image'
import { lineNumberPlugin } from './plugins/lineNumbers'
import { preWrapperPlugin } from './plugins/preWrapper'
import { gitHubAlertsPlugin } from './plugins/githubAlerts'

export type ThemeOptions =
  | ThemeRegistrationAny
  | BuiltinTheme
  | {
      light: ThemeRegistrationAny | BuiltinTheme
      dark: ThemeRegistrationAny | BuiltinTheme
    }

export interface MarkdownOptions extends MarkdownIt.Options {
  /* ==================== General Options ==================== */

  /**
   * Setup markdown-it instance before applying plugins
   */
  preConfig?: (md: MarkdownIt) => void
  /**
   * Setup markdown-it instance
   */
  config?: (md: MarkdownIt) => void
  /**
   * Disable cache (experimental)
   */
  cache?: boolean
  externalLinks?: Record<string, string>

  /* ==================== Syntax Highlighting ==================== */

  /**
   * Custom theme for syntax highlighting.
   *
   * You can also pass an object with `light` and `dark` themes to support dual themes.
   *
   * @example { theme: 'github-dark' }
   * @example { theme: { light: 'github-light', dark: 'github-dark' } }
   *
   * You can use an existing theme.
   * @see https://shiki.style/themes
   * Or add your own theme.
   * @see https://shiki.style/guide/load-theme
   */
  theme?: ThemeOptions
  /**
   * Languages for syntax highlighting.
   * @see https://shiki.style/languages
   */
  languages?: LanguageInput[]
  /**
   * Custom language aliases.
   *
   * @example { 'my-lang': 'js' }
   * @see https://shiki.style/guide/load-lang#custom-language-aliases
   */
  languageAlias?: Record<string, string>
  /**
   * Show line numbers in code blocks
   * @default false
   */
  lineNumbers?: boolean
  /**
   * Fallback language when the specified language is not available.
   */
  defaultHighlightLang?: string
  /**
   * Transformers applied to code blocks
   * @see https://shiki.style/guide/transformers
   */
  codeTransformers?: ShikiTransformer[]
  /**
   * Setup Shiki instance
   */
  shikiSetup?: (shiki: Highlighter) => void | Promise<void>

  /* ==================== Markdown It Plugins ==================== */

  /**
   * Options for `markdown-it-anchor`
   * @see https://github.com/valeriangalliat/markdown-it-anchor
   */
  anchor?: anchorPlugin.AnchorOptions
  /**
   * Options for `markdown-it-attrs`
   * @see https://github.com/arve0/markdown-it-attrs
   */
  attrs?: {
    leftDelimiter?: string
    rightDelimiter?: string
    allowedAttributes?: Array<string | RegExp>
    disable?: boolean
  }
  /**
   * Options for `markdown-it-emoji`
   * @see https://github.com/markdown-it/markdown-it-emoji
   */
  emoji?: {
    defs?: Record<string, string>
    enabled?: string[]
    shortcuts?: Record<string, string | string[]>
  }
  /**
   * Options for `@mdit-vue/plugin-frontmatter`
   * @see https://github.com/mdit-vue/mdit-vue/tree/main/packages/plugin-frontmatter
   */

  /**
   * Options for `markdown-it-container`
   * @see https://github.com/markdown-it/markdown-it-container
   */
  container?: ContainerOptions
  /**
   * Math support (experimental)
   *
   * You need to install `markdown-it-mathjax3` and set `math` to `true` to enable it.
   * You can also pass options to `markdown-it-mathjax3` here.
   * @default false
   * @see https://vitepress.dev/guide/markdown#math-equations
   */
  math?: boolean | any
  image?: ImageOptions
  /**
   * Allows disabling the github alerts plugin
   * @default true
   * @see https://vitepress.dev/guide/markdown#github-flavored-alerts
   */
  gfmAlerts?: boolean
}

export type MarkdownRenderer = MarkdownIt

export const createMarkdownRenderer = async (
  srcDir: string,
  options: MarkdownOptions = {},
  base = '/',
  logger: Pick<Logger, 'warn'> = console
): Promise<MarkdownRenderer> => {
  const theme = options.theme ?? { light: 'github-light', dark: 'github-dark' }
  const hasSingleTheme = typeof theme === 'string' || 'name' in theme

  const md = MarkdownIt({
    html: true,
    linkify: true,
    highlight: options.highlight || (await highlight(theme, options, logger)),
    ...options
  })

  md.linkify.set({ fuzzyLink: false })

  if (options.preConfig) {
    options.preConfig(md)
  }

  // custom plugins
  md.use(highlightLinePlugin)
    .use(preWrapperPlugin, { hasSingleTheme })
    .use(containerPlugin, { hasSingleTheme }, options.container)
    .use(imagePlugin, options.image)
    .use(lineNumberPlugin, options.lineNumbers)

  if (options.gfmAlerts !== false) {
    md.use(gitHubAlertsPlugin)
  }

  // 3rd party plugins
  if (!options.attrs?.disable) {
    md.use(attrsPlugin, options.attrs)
  }
  md.use(emojiPlugin, { ...options.emoji })


  if (options.math) {
    try {
      const mathPlugin = await import('markdown-it-mathjax3')
      md.use(mathPlugin.default ?? mathPlugin, {
        ...(typeof options.math === 'boolean' ? {} : options.math)
      })
    } catch (error) {
      throw new Error(
        'You need to install `markdown-it-mathjax3` to use math support.'
      )
    }
  }

  // apply user config
  if (options.config) {
    options.config(md)
  }

  return md
}
