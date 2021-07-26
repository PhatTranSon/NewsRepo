const Sequelize = require("sequelize");

const NewsModel = (sequelize) => {
    //Create and initialize model
    class News extends Sequelize.Model {}
    News.init({
        id: {
            type: Sequelize.DataTypes.INTEGER,
            primaryKey: true,
            field: "id"
        },
        title: {
            type: Sequelize.DataTypes.STRING(255)
        },
        image: {
            type: Sequelize.DataTypes.STRING(500)
        },
        text: {
            type: Sequelize.DataTypes.TEXT
        },
        authors: {
            type: Sequelize.DataTypes.TEXT
        },
        url: {
            type: Sequelize.DataTypes.STRING(500)
        },
        date: {
            type: Sequelize.DataTypes.DATE
        }
    }, {
        sequelize,
        modelName: "article",
        tableName: "articles",
        timestamps: false //Disable timestamp for createdAt and updatedAt fields
    });
}

module.exports = NewsModel;