EXAMPLE_TEXT = """TITLE: Why Computers are Stupid
DESCRIPTION: The phrase "computers are stupid" refers 
to how they interpret instructions literally. This 
means that small typos can cause big problems.
TITLE: Python
DESCRIPTION: Python is a "programming language." It 
provides programmers a way to write instructions for a 
computer to execute in a way that the computer can understand.
TITLE: While Loops
DESCRIPTION: A while loop repeatedly executes the body of
the loop until the "test condition" is no longer true."""

# This function breaks out the title for each concept.

def get_title(concept):
    start_location = concept.find('TITLE:')
    end_location = concept.find('DESCRIPTION:')
    title = concept[start_location+7 : end_location-1]
    return title

# This function breaks out the description for each concept.
	
def get_description(concept):
    start_location = concept.find('DESCRIPTION:')
    description = concept[start_location+13 :]
    return description   

# This function converts the text format to a list with elements containing a title and a description

def convert_text_to_list(text):
	concept_pair = []
	counter = 0
	concept_number = text.count('TITLE:')
#	print concept_number
	while counter < concept_number:
		next_concept_start = text.find('TITLE:')
		next_concept_end   = text.find('TITLE:', next_concept_start + 1)
		concept = text[next_concept_start:next_concept_end]
		text = text[next_concept_end:]
		title = get_title(concept)
		description = get_description(concept)
		concept_pair = [title,description]
		counter = counter + 1
		html_concept_list.append(concept_pair)
	return concept_pair

	
html_concept_list = []	
concept = convert_text_to_list(EXAMPLE_TEXT)

#print html_concept_list

# This section takes the new list and converts it to HTML.

def generate_concept_HTML(concept_title, concept_description):
    html_text_1 = '''
<div class="concept">
    <div class="concept-title">
        ''' + concept_title
    html_text_2 = '''
    </div>
    <div class="concept-description">
        ''' + concept_description
    html_text_3 = '''
    </div>
</div>'''
    full_html_text = html_text_1 + html_text_2 + html_text_3
    return full_html_text

def make_HTML(concept):
    concept_title = concept[0]
    concept_description = concept[1]
    return generate_concept_HTML(concept_title, concept_description)


def make_HTML_for_many_concepts(list_of_concepts):
    HTML = ""
    for concept in list_of_concepts:
        concept_HTML = make_HTML(concept)
        HTML = HTML + concept_HTML
    return HTML

print make_HTML_for_many_concepts(html_concept_list)
