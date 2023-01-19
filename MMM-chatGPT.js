Module.register("MMM-chatGPT", {
  // Default module config.
  defaults: {
    text: "Det var en gang en kar, som het Nils. Han gikk nedover torget en solskinnsdag i Januar.",
  },

  getTemplate: function () {
    return "MMM-chatGPT.njk";
  },

  getTemplateData: function () {
    return this.config;
  }
});