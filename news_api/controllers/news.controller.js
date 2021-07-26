const { models } = require("../models/index");

//Controller
const getNews = async (req, resp) => {
    //Find all news
    const news = await models.article.findAll();
    //Display
    resp.status(200).json(news);
}

module.exports = {
    getNews
}
