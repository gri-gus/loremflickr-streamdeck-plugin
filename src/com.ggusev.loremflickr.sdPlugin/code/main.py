import requests
from streamdeck_sdk import (
    StreamDeck,
    Action,
    events_received_objs,
    events_sent_objs,
    image_bytes_to_base64,
    logger,
)

import settings


class LoremFlickrError(Exception):
    pass


def get_image_from_lorem_flickr(
        category: str,
        union_type: str = "or",
        grayscale_flag: bool = False,
        timeout: float = 5,
) -> str:
    url = settings.LOREM_FLICKR_URL
    if grayscale_flag:
        url += "/g"
    url += f"/{settings.IMAGE_SIZE}/{settings.IMAGE_SIZE}/{category}"
    if union_type == "and":
        url += "/all"
    logger.info(f"{url=}")
    response = requests.get(url, stream=True, timeout=timeout)
    if not response.ok:
        raise LoremFlickrError(f"Bad response. Status code: {response.status_code}")
    image_binary = response.content
    image_mime = response.headers["Content-Type"]
    image_base64 = image_bytes_to_base64(obj=image_binary, image_mime=image_mime)
    return image_base64


class SetKeyImage(Action):
    UUID = "com.ggusev.loremflickr.setkeyimage"

    def on_key_down(self, obj: events_received_objs.KeyDown):
        category = obj.payload.settings.get("category", "kitten")
        union_type = obj.payload.settings.get("union_type", "or")
        grayscale_flag = obj.payload.settings.get("grayscale_flag", False)

        logger.info(f"{category=}, {union_type=}, {grayscale_flag=}")
        try:
            image_base64 = get_image_from_lorem_flickr(
                category=category,
                union_type=union_type,
                grayscale_flag=grayscale_flag,
            )
        except Exception as err:  # noqa
            logger.error(str(err))
            self.show_alert(context=obj.context)
            return

        self.set_image(
            context=obj.context,
            payload=events_sent_objs.SetImagePayload(
                image=image_base64,
                target=0,
                state=obj.payload.state,
            )
        )


if __name__ == '__main__':
    StreamDeck(
        actions=[
            SetKeyImage(),
        ],
        log_file=settings.LOG_FILE_PATH,
        log_level=settings.LOG_LEVEL,
        log_backup_count=1,
    ).run()
