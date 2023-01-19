Module.register("MMM-chatGPT", {
  // Default module config.
  defaults: {
    text: "Hello World!",
  },

  getTemplate: function () {
    return "MMM-chatGPT.njk";
  },

  getTemplateData: function () {
    return this.config;
  }
});