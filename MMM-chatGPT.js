Module.register("MMM-chatGPT", {
  // Default module config.
  defaults: {
    text: "Hei Dominic :)",
  },

  getTemplate: function () {
    return "MMM-chatGPT.njk";
  },

  getTemplateData: function () {
    return this.config;
  }
});