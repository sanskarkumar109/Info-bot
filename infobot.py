from IPython.display import Markdown
from PIL import Image
import textwrap
import google.generativeai as GenAI

# Function to convert text to Markdown format
def to_markdown(text):
    """
    Convert plain text to Markdown format.

    Args:
        text (str): The plain text.

    Returns:
        Markdown: The formatted text in Markdown.
    """
    text = text.replace(".", " *")
    return Markdown(textwrap.indent(text, "> ", predicate=lambda _: True))


# Function to get responses for questions
def get_gemini_response_question(question):
    """
    Get Gemini response for a given question.

    Args:
        question (str): The input question.

    Returns:
        str: The Gemini response.
    """
    model = GenAI.GenerativeModel("gemini-1.5-flash")  # Update model to gemini-1.5-flash
    response = model.generate_content(question)
    return response.text


# Function to get responses for images
def get_gemini_response_image(input_text, image):
    """
    Get Gemini response for a given image.

    Args:
        input_text (str): The input prompt text.
        image (Image): The uploaded image.

    Returns:
        str: The Gemini response.
    """
    model = GenAI.GenerativeModel('gemini-1.5-flash')  # Update model to gemini-1.5-flash
    if input_text != "":
        response = model.generate_content([input_text, image])
    else:
        response = model.generate_content(image)
    return response.text





