import os


def generate_invitations(template, attendees):
    
        if not isinstance(template,str) or not isinstance(attendees,list):
            raise TypeError()
        
        if template.strip() == "" :
            print("Template is empty, no output files generated.")
            return
        if len(attendees) == 0:
            print("No data provided, no output files generated.")
            return

        for i, attendee in enumerate(attendees, start=1):
            for key, value in attendee.items():
                if value is None:
                    attendee[key] = "N/A"
            try:
                letter = template.format(**attendee)
            except  KeyError as e:
                raise Exception(f"Missing placeholder in attendee data: {e}")

            with open(f"output_{i}.txt", "w", encoding="utf-8") as file:
                file.write(letter)
            
