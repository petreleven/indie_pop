from quart import Quart, request, render_template
import os


app = Quart(__name__)


# set template and static folder
template_folder = os.path.join(os.getcwd(), "templates/")
static_folder = os.path.join(os.getcwd(), "static/")
app.template_folder = template_folder
app.static_folder = static_folder


@app.get("/")
async def index():
    return await render_template(
        template_name_or_list="index.html",
        context={"topTableOverviews": [1, 2, 3], "bottomTableOverviews": [1, 2, 3]},
    )


@app.get("/channels/<string:genres>")
async def channel_genres(genres):
    return await render_template(
        template_name_or_list="channels.html",
        context={"channels": [i for i in range(30)]},
    )


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5500, debug=True)
