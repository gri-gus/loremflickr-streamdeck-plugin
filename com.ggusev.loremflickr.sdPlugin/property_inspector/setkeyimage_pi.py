from pathlib import Path

from streamdeck_sdk_pi import *

OUTPUT_DIR = Path(__file__).parent
TEMPLATE = Path(__file__).parent / "pi_template.html"


class LoremFlickrStatus(BasePIElement):
    def get_html_element(self) -> str:
        res = """
    <div class="sdpi-item" style="max-height: 60px">
        <div class="sdpi-item-label">Website status</div>
        <div class="sdpi-item-value"
             style="background: #3D3D3D; height:26px; max-width: 56px; margin: 0 0 0 5px; padding: 0">
            <img src="https://img.shields.io/website?down_color=%233d3d3d&down_message=offline&label=&style=flat-square&up_color=%233d3d3d&up_message=online&url=https%3A%2F%2Floremflickr.com%2F"
                 alt="" style="height: 26px; max-width: 56px; margin: 0">
        </div>
    </div>
        """
        return res


def main():
    pi = PropertyInspector(
        action_uuid="com.ggusev.loremflickr.setkeyimage",
        elements=[
            LoremFlickrStatus(),
            Heading(label="SETTINGS"),
            Textfield(
                label="Category",
                uid="category",
                required=True,
                placeholder="Enter category",
                default_value="kitten",
                pattern=r"^[a-zA-Z0-9,]{2,}$"
            ),
            Radio(
                label="Union type",
                uid="union_type",
                items=[
                    RadioItem(value="or", label="or", checked=True),
                    RadioItem(value="and", label="and", checked=False),
                ]
            ),
            Checkbox(
                label="Grayscale",
                items=[
                    CheckboxItem(uid="grayscale_flag", checked=False, ),
                ]
            ),
            Details(
                uid="manual_message",
                heading="Manual",
                text="""
    Category: Enter a word or words separated by commas to search for the image. This field does not accept spaces.
    Union type: If you have entered more than one word in the "Category" field, then select as the union option. \
    If "and" is selected, images matching all the specified words will be searched. If "or" is selected, \
    images matching at least one of the words will be searched.
    Grayscale: Check the box if you want the image to be grayscale.
                    """,
                full_width=False,
                default_open=False,
            ),
        ]
    )
    pi.build(output_dir=OUTPUT_DIR, template=TEMPLATE)


if __name__ == '__main__':
    main()
