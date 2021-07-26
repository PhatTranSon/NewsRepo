import { DataTypes, Model } from "sequelize";

const NewsModel = (sequelize) => {
    //Create and initialize model
    class News extends Model {}
    News.init({
        id: {
            type: DataTypes.INTEGER,
            field: "id"
        },
        title: {
            type: DataTypes.STRING(255)
        },
        image: {
            type: DataTypes.STRING(500)
        },
        text: {
            type: DataTypes.TEXT
        },
        authors: {
            type: DataTypes.TEXT
        },
        url: {
            type: DataTypes.STRING(500)
        },
        date: {
            type: DataTypes.DATE
        }
    }, {
        sequelize,
        modelName: "article",
        tableName: "articles"
    });
}

export default NewsModel;