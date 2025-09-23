import os
# Write the Templating Function:
def generate_invitations (template, attendees):
    try:
        if type(template) is not str or type(attendees) is not list:
            raise Exception(SyntaxError)
        if template.strip() == "":
            raise Exception('template is empty')
        if len(attendees) == 0:
            raise Exception('attendence is empty')
        for attendee in attendee:
            template.format(**attendee)
    except:
        raise Exception()

    # Process Each Attendee:
    #     Iterate over the list of attendees and replace the placeholders in the template with the corresponding values from each attendee’s dictionary.
    #     If a value is missing, replace it with “N/A”.

    # Generate Output Files:
    #     Write the processed template to output files named output_X.txt, where X is the index of the attendee starting from 1.

    # Specific Error Handling Behaviors:
    #     Empty Template: If the template is empty, log an error message, “Template is empty, no output files generated.” and terminate without creating any files.
    #     Empty List of Objects: If the list of objects is empty, log a message, “No data provided, no output files generated.” and terminate without creating any files.
    #     Missing Data in Object: If an object is missing data for any of the placeholders, replace the missing data with the text “N/A” in the output file. For example, if event_date is missing, it should appear as “event_date: N/A” in the output.
    #     Invalid Input Types: If the input template is not a string or the list is not a list of dictionaries, log an error message indicating the type of invalid input and terminate the function.
