module.exports = (handler) => {
    return async (req, resp, next) => {
        try {
            await handler(req, resp);
        } catch (error) {
            next(error);
        }
    }
}