const {getSidebarData} = require("../utils.mjs");


module.exports = (options, ctx) => ({
  async enhanceAppFiles() {
    const data = getSidebarData();
    return `
      export default ({ siteData }) => {
        siteData.themeConfig = {
          ...siteData.themeConfig,
          sidebar: ${JSON.stringify(data)}
        };
      };
    `;
  }
});