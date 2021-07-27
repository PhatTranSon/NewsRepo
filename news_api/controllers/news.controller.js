const { sequelize, Sequelize } = require("../models/index");
const { models } = sequelize;
const { Op } = Sequelize;

//Controllers
const getAllNews = async (req, resp) => {
    //Get limit and after id parameters
    const limit = Number(req.query.limit) || 10;
    const after_id = Number(req.query.after_id) || 0;

    //Find all news
    const news = await models.article.findAll({
        where: {
            id: {
                [Op.gte]: after_id 
            }
        },
        limit: limit
    });

    //Display
    resp.status(200).json(news);
}

const getOneNews = async (req, resp) => {
    //Get params
    const { newsId } = req.params;
    const news = await models.article.findByPk(newsId);

    if (news) {
        resp.status(200).json(news);
    } else {
        resp.status(404).json({
            message: "Item not found"
        });
    }
}

module.exports = {
    getAllNews,
    getOneNews
}
