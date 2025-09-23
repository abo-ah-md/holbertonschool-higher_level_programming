import os

def generate_invitations(template, attendees):
    """
    Generates personalized invitation files based on a template and attendees list.
    - template: str containing placeholders {name}, {event_title}, {event_date}, {event_location}
    - attendees: list of dictionaries containing attendee data
    """

    # --- Input Type Checks ---
    if not isinstance(template, str):
        raise Exception("Invalid input: template must be a string.")

    if not isinstance(attendees, list) or not all(isinstance(a, dict) for a in attendees):
        raise Exception("Invalid input: attendees must be a list of dictionaries.")

    # --- Empty Input Checks ---
    if template.strip() == "":
        raise Exception("Template is empty, no output files generated.")

    if len(attendees) == 0:
        raise Exception("No data provided, no output files generated.")

    # --- Process Each Attendee ---
    for i, attendee in enumerate(attendees, start=1):
        # Replace None with 'N/A'
        clean_attendee = {k: (v if v is not None else "N/A") for k, v in attendee.items()}

        try:
            # Format invitation using placeholders
            letter = template.format(**clean_attendee)
        except KeyError as e:
            raise Exception(f"Missing placeholder in attendee data: {e}")

        # --- Create Output File ---
        filename = f"output_{i}.txt"
        with open(filename, "w", encoding="utf-8") as file:
            file.write(letter)
