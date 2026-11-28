"""Starter learning resources for the Study Hub year-level library."""

import random


SUBJECTS = [
    {'slug': 'maths', 'name': 'Maths', 'icon': '∑', 'tone': 'maths'},
    {'slug': 'english', 'name': 'English', 'icon': 'Aa', 'tone': 'english'},
    {'slug': 'science', 'name': 'Science', 'icon': '✳', 'tone': 'science'},
]


def question(prompt, options, answer, explanation):
    return {
        'prompt': prompt,
        'options': options,
        'answer': answer,
        'explanation': explanation,
    }


def lesson(topic, notes, article, questions):
    return {
        'topic': topic,
        'notes': notes,
        'article': article,
        'questions': questions,
    }


# Each year and subject has its own notes, short article, and question bank.
YEAR_CONTENT = {
    1: {
        'maths': lesson('Counting and adding',
            ['Count objects one at a time.', 'Addition joins groups; subtraction takes some away.'],
            'Numbers help us describe how many things there are. When two small groups join, we can count them together to find the total.', [
                question('There are 4 red blocks and 3 blue blocks. How many blocks are there?', ['6', '7', '8'], 1, '4 + 3 = 7 blocks.'),
                question('Which number comes just before 12?', ['11', '10', '13'], 0, 'Counting backwards from 12 gives 11.'),
                question('Which shape has three sides?', ['A circle', 'A square', 'A triangle'], 2, 'A triangle has three straight sides.'),
            ]),
        'english': lesson('Sounds and sentences',
            ['A sentence begins with a capital letter.', 'A full stop shows where a telling sentence ends.'],
            'Letters stand for sounds, and sounds join to make words. Words can be put together to tell a reader a complete idea.', [
                question('Which sentence begins correctly?', ['the dog can run.', 'The dog can run.', 'the Dog can run.'], 1, 'A sentence starts with a capital letter.'),
                question('Which word rhymes with “sun”?', ['sit', 'run', 'sand'], 1, '“Sun” and “run” share the ending sound.'),
                question('Which mark can end a telling sentence?', ['A full stop (.)', 'A comma (,)', 'A capital letter'], 0, 'A full stop marks the end of a telling sentence.'),
            ]),
        'science': lesson('Living things',
            ['Living things grow and need resources such as water and food.', 'Plants need light and water to grow.'],
            'A garden is home to many living things. Plants grow from seeds, while animals find food and water in the places where they live.', [
                question('Which one is a living thing?', ['A rock', 'A tree', 'A cup'], 1, 'A tree grows and needs water and light.'),
                question('What do plants use from sunlight?', ['Light energy', 'Sand', 'Metal'], 0, 'Plants use light energy to help them make food.'),
                question('Which need do people and animals share?', ['Water', 'A shell', 'A nest'], 0, 'People and animals both need water.'),
            ]),
    },
    2: {
        'maths': lesson('Place value to 100',
            ['A two-digit number has tens and ones.', 'Ten ones can be regrouped as one ten.'],
            'Place value gives each digit a job. In 46, the 4 stands for four tens and the 6 stands for six ones.', [
                question('What is 40 + 6?', ['406', '46', '64'], 1, 'Four tens and six ones make 46.'),
                question('What is 32 + 15?', ['47', '48', '57'], 0, 'Add the tens and ones: 32 + 15 = 47.'),
                question('Which number is even?', ['15', '17', '18'], 2, '18 is even because it can be split into two equal groups.'),
            ]),
        'english': lesson('Verbs and story order',
            ['A verb tells what someone or something does.', 'Stories often have a beginning, a middle, and an ending.'],
            'A clear story helps readers follow what happens. Action verbs such as “raced” or “whispered” help us picture each moment.', [
                question('Which word is a verb?', ['bright', 'jumped', 'pencil'], 1, '“Jumped” describes an action.'),
                question('What usually comes first in a story?', ['The ending', 'The beginning', 'The middle'], 1, 'The beginning introduces the story.'),
                question('Which word best describes a tiny mouse?', ['enormous', 'small', 'loudly'], 1, '“Small” describes the mouse.'),
            ]),
        'science': lesson('Materials and their properties',
            ['Objects are made from materials such as wood, glass, and metal.', 'A material’s properties help decide what it is useful for.'],
            'A window is often made from glass because glass lets light pass through. A spoon is often made from metal because metal is strong and keeps its shape.', [
                question('Which material is usually transparent?', ['Glass', 'Cardboard', 'Clay'], 0, 'Clear glass lets light pass through so we can see through it.'),
                question('Which material is usually a good choice for a raincoat?', ['Paper', 'Waterproof fabric', 'Dry sand'], 1, 'Waterproof fabric helps keep rain away.'),
                question('Which property describes a material that bends easily?', ['Flexible', 'Magnetic', 'Transparent'], 0, 'A flexible material can bend without breaking easily.'),
            ]),
    },
    3: {
        'maths': lesson('Multiplication and equal groups',
            ['Multiplication is a quick way to count equal groups.', 'Division shares a total into equal groups.'],
            'Arrays show multiplication in rows and columns. Three rows of four counters make 3 × 4, or 12 counters altogether.', [
                question('What is 4 × 3?', ['10', '11', '12'], 2, 'Four groups of three make 12.'),
                question('What is 24 ÷ 6?', ['4', '5', '6'], 0, 'Six equal groups of 4 make 24.'),
                question('What is one half of 10?', ['4', '5', '6'], 1, 'Sharing 10 equally into two groups gives 5 in each.'),
            ]),
        'english': lesson('Paragraphs and description',
            ['A paragraph groups sentences about one main idea.', 'Adjectives describe nouns and can help readers imagine a scene.'],
            'Writers choose details that help readers build a picture. A paragraph about a beach might describe the warm sand, rolling waves, and salty air.', [
                question('Which word is an adjective in “the bright kite flew”?', ['flew', 'the', 'bright'], 2, '“Bright” describes the kite.'),
                question('What should sentences in a paragraph mostly share?', ['One main idea', 'Different topics', 'No connection'], 0, 'A paragraph is easier to follow when its sentences share a main idea.'),
                question('Which word is a noun?', ['quickly', 'river', 'soft'], 1, 'A river is a person, place, or thing, so it is a noun.'),
            ]),
        'science': lesson('States of matter',
            ['Solids keep their shape; liquids flow and take the shape of a container.', 'Heating or cooling can change a material from one state to another.'],
            'Ice is solid water. When it warms, it melts into liquid water; with more heating, water can evaporate into an invisible gas called water vapour.', [
                question('What happens when ice melts?', ['It becomes liquid water', 'It becomes a metal', 'It disappears forever'], 0, 'Melting changes solid ice into liquid water.'),
                question('Which state of matter flows to fill its container?', ['Solid', 'Liquid', 'Rock'], 1, 'A liquid flows and takes the shape of its container.'),
                question('What can heating liquid water produce?', ['Water vapour', 'Ice straight away', 'Wood'], 0, 'Heating can evaporate liquid water into water vapour.'),
            ]),
    },
    4: {
        'maths': lesson('Fractions and measurement',
            ['A fraction names equal parts of a whole.', 'Perimeter is the distance around a shape.'],
            'Fractions make sharing easier to describe. If a shape is split into four equal parts, each part is one quarter; three of those parts are three quarters.', [
                question('What is 3/4 of 8?', ['4', '6', '7'], 1, 'One quarter of 8 is 2, so three quarters is 2 × 3 = 6.'),
                question('How many centimetres are in 2.5 metres?', ['25 cm', '205 cm', '250 cm'], 2, 'Each metre is 100 cm, so 2.5 metres is 250 cm.'),
                question('A square has sides of 3 cm. What is its perimeter?', ['9 cm', '12 cm', '15 cm'], 1, 'A square has four equal sides: 4 × 3 = 12 cm.'),
            ]),
        'english': lesson('Inference and evidence',
            ['An inference is an idea based on clues in a text.', 'Use a detail from the text to support your thinking.'],
            'Writers do not always explain every feeling directly. A character who grips an umbrella and watches dark clouds may be worried about the weather.', [
                question('A character grips an umbrella as clouds gather. What is a reasonable inference?', ['They expect rain', 'They are underwater', 'It is midnight'], 0, 'The umbrella and clouds are clues that rain may be coming.'),
                question('What makes an inference stronger?', ['A clue from the text', 'A random guess', 'Ignoring the story'], 0, 'A text detail gives evidence for an inference.'),
                question('Which sentence uses quotation marks correctly?', ['“I am ready,” said Lee.', 'I am “ready, said Lee.', '“I am ready, said Lee.'], 0, 'Quotation marks go around the spoken words.'),
            ]),
        'science': lesson('Food chains and habitats',
            ['A habitat is a place where an organism gets what it needs.', 'A food chain shows how energy moves from one living thing to another.'],
            'In a meadow, grass can use sunlight to grow. A rabbit may eat the grass, and a fox may eat the rabbit, passing energy along the food chain.', [
                question('Which organism is a producer in this chain: grass → rabbit → fox?', ['Grass', 'Rabbit', 'Fox'], 0, 'Grass makes its own food using light, so it is a producer.'),
                question('What does a habitat provide?', ['Needs such as food and shelter', 'Only sunlight', 'A guaranteed escape from predators'], 0, 'Habitats provide resources organisms need to survive.'),
                question('Where does most food-chain energy begin?', ['The Sun', 'The Moon', 'A rock'], 0, 'Plants capture energy from sunlight.'),
            ]),
    },
    5: {
        'maths': lesson('Decimals and area',
            ['Decimal places show tenths, hundredths, and smaller parts.', 'Area measures the surface inside a 2D shape.'],
            'Money is one familiar place to see decimals: 75 cents is $0.75. For a rectangle, multiplying its length by its width gives its area.', [
                question('What is 0.4 + 0.35?', ['0.39', '0.75', '0.435'], 1, 'Write 0.4 as 0.40, then 0.40 + 0.35 = 0.75.'),
                question('What is the area of a 3 cm by 8 cm rectangle?', ['11 cm²', '22 cm²', '24 cm²'], 2, 'Area = length × width = 8 × 3 = 24 cm².'),
                question('Which decimal is equal to 3/5?', ['0.3', '0.6', '0.8'], 1, '3 ÷ 5 = 0.6.'),
            ]),
        'english': lesson('Persuasion and point of view',
            ['Persuasive writing gives reasons for a point of view.', 'A writer may use examples, facts, and emotive words to influence readers.'],
            'A school garden proposal can persuade by explaining its benefits. A writer might combine a fact about plants with a personal example about caring for seedlings.', [
                question('Which sentence gives a reason?', ['Gardens are green.', 'A garden can give students a place to grow fresh herbs.', 'Look at that!'], 1, 'It explains a benefit that supports the proposal.'),
                question('Which is an emotive word?', ['enormous', 'devastating', 'table'], 1, '“Devastating” is chosen to create a strong feeling.'),
                question('Why should a persuasive writer use evidence?', ['To support a claim', 'To hide the main idea', 'To make every sentence longer'], 0, 'Evidence helps readers see why a claim may be convincing.'),
            ]),
        'science': lesson('Ecosystems and the water cycle',
            ['An ecosystem includes living things and their non-living environment.', 'Water moves through evaporation, condensation, and precipitation.'],
            'Sunlight warms water in oceans and lakes, causing some of it to evaporate. Higher in the sky, water vapour cools into droplets that can form clouds and later fall as rain.', [
                question('What is evaporation?', ['Liquid water changing into vapour', 'Clouds turning into rocks', 'Rain soaking into a leaf'], 0, 'Evaporation changes liquid water into water vapour.'),
                question('What is an ecosystem?', ['Living things and their environment', 'Only one animal', 'A weather forecast'], 0, 'An ecosystem includes organisms and the non-living parts of their surroundings.'),
                question('What often forms when water vapour cools?', ['Water droplets', 'Dry sand', 'Metal'], 0, 'Cooling vapour condenses into tiny liquid droplets.'),
            ]),
    },
    6: {
        'maths': lesson('Percentages, ratios, and integers',
            ['Percent means “out of 100”.', 'A ratio compares amounts; integers include negative whole numbers.'],
            'Percentages are useful for comparing parts of a whole. Ratios describe how quantities relate, while negative integers can describe values below zero.', [
                question('What is 20% of 60?', ['6', '12', '20'], 1, '10% of 60 is 6, so 20% is 12.'),
                question('The ratio of red to blue beads is 2:3 and there are 25 beads. How many are red?', ['10', '12', '15'], 0, 'There are 5 equal parts; each is 5 beads, so red beads = 2 × 5 = 10.'),
                question('What is -4 + 9?', ['-13', '4', '5'], 2, 'Moving 9 places right from -4 gives 5.'),
            ]),
        'english': lesson('Audience, tone, and evidence',
            ['Audience is the reader or listener a text is made for.', 'Tone is the attitude created by word choice and sentence style.'],
            'The same idea can sound different for different audiences. A message to a friend might be casual, while a letter to a council needs a more formal tone and clear evidence.', [
                question('Which opening is most suitable for a formal letter to a council?', ['Hey there!', 'Dear Council Members,', 'Yo!'], 1, 'It uses a respectful, formal greeting for that audience.'),
                question('Which sentence is an opinion?', ['The meeting starts at 3 pm.', 'The park is the best place in town.', 'The notice lists three dates.'], 1, '“Best” expresses a judgement rather than a checkable fact.'),
                question('What can evidence do in an argument?', ['Support a point', 'Replace the topic', 'Change the audience'], 0, 'Evidence gives support for an idea or claim.'),
            ]),
        'science': lesson('Electric circuits and energy',
            ['A simple circuit needs a complete path for electric current.', 'Energy can be transferred and changed from one form to another.'],
            'In a battery circuit, electrical energy moves through wires to a component such as a lamp. The lamp transfers some of that energy into light and heat.', [
                question('What happens if a switch opens the circuit?', ['The complete path is broken', 'The battery becomes a wire', 'The lamp makes more current'], 0, 'An open switch breaks the path, so current cannot flow around the circuit.'),
                question('What energy change happens in a lit lamp?', ['Electrical to light and heat', 'Sound to chemical', 'Heat to water'], 0, 'A lamp transfers electrical energy into light and heat.'),
                question('Which material usually allows current to flow?', ['Copper', 'Rubber', 'Dry wood'], 0, 'Copper is a good electrical conductor.'),
            ]),
    },
    7: {
        'maths': lesson('Integers and simple equations',
            ['Integers lie on a number line and include negative numbers.', 'To solve an equation, keep both sides balanced.'],
            'A number line makes integer addition easier to picture. Solving 3x + 2 = 14 means undoing the addition and multiplication while keeping the equation balanced.', [
                question('What is -3 + 8?', ['-11', '5', '11'], 1, 'Starting at -3 and moving 8 places right lands on 5.'),
                question('Solve 3x + 2 = 14.', ['x = 3', 'x = 4', 'x = 5'], 1, 'Subtract 2 to get 3x = 12, then divide by 3.'),
                question('What is 5/8 - 1/8?', ['1/2', '4/16', '6/8'], 0, 'The denominators match: 5/8 - 1/8 = 4/8 = 1/2.'),
            ]),
        'english': lesson('Metaphor and paragraph structure',
            ['A metaphor describes one thing as another to suggest a shared quality.', 'A topic sentence introduces a paragraph’s main point.'],
            '“The classroom was a beehive” is a metaphor that suggests busy movement and sound. A strong paragraph then develops one clear idea with details or examples.', [
                question('What does “the classroom was a beehive” most likely suggest?', ['It was busy and buzzing', 'It was made of honey', 'It was empty'], 0, 'The comparison to a beehive suggests lots of busy activity.'),
                question('What is a topic sentence for?', ['To introduce the main idea', 'To list every punctuation mark', 'To end a whole book'], 0, 'A topic sentence tells readers the paragraph’s focus.'),
                question('Which sentence is a metaphor?', ['The rain fell softly.', 'Her idea was a seed.', 'He ran like the wind.'], 1, 'It describes the idea as a seed; “like” would make the third a simile.'),
            ]),
        'science': lesson('Cells and forces',
            ['Cells are the basic units that make up living organisms.', 'A force is a push or pull that can change an object’s motion.'],
            'A plant and an animal are built from cells, though their cells have different structures. A force such as friction can slow a moving object when two surfaces rub together.', [
                question('What is a cell?', ['A basic unit of living things', 'A type of force', 'A star'], 0, 'Cells are the basic units that make up organisms.'),
                question('What can friction do to a sliding object?', ['Slow it down', 'Turn it into a liquid', 'Remove its mass'], 0, 'Friction opposes motion between touching surfaces.'),
                question('Which structure is found in plant cells and helps capture light?', ['Chloroplast', 'Lung', 'Bone'], 0, 'Chloroplasts contain chlorophyll, which absorbs light for photosynthesis.'),
            ]),
    },
    8: {
        'maths': lesson('Expanding expressions and percentages',
            ['Use the distributive law to multiply a number by every term in brackets.', 'Find a percentage by converting it to a fraction or decimal.'],
            'Expanding 3(x + 2) means multiplying 3 by both terms inside the brackets. Percentages also describe change: 15% of 200 is a part of the original 200.', [
                question('Expand 3(x + 2).', ['3x + 2', '3x + 6', 'x + 6'], 1, 'Multiply both terms by 3: 3 × x + 3 × 2 = 3x + 6.'),
                question('What is 15% of 200?', ['15', '30', '45'], 1, '10% of 200 is 20 and 5% is 10, giving 30.'),
                question('A line rises 6 units while moving 3 units right. What is its gradient?', ['2', '3', '18'], 0, 'Gradient = rise ÷ run = 6 ÷ 3 = 2.'),
            ]),
        'english': lesson('Comparing viewpoints and voice',
            ['A text’s perspective is the position or viewpoint it presents.', 'Active and passive voice place emphasis on different parts of a sentence.'],
            'Two writers can describe the same event from different perspectives. “The team designed the poster” is active; “The poster was designed by the team” shifts attention to the poster.', [
                question('Which sentence uses passive voice?', ['The storm closed the road.', 'The road was closed by the storm.', 'The storm is coming.'], 1, 'The subject “road” receives the action in “was closed”.'),
                question('What does comparing two viewpoints help you notice?', ['Different choices and priorities', 'That both texts must be identical', 'Only spelling'], 0, 'Viewpoints can reveal different priorities or interpretations.'),
                question('What does the word “frugal” usually suggest?', ['Careful with money', 'Very noisy', 'Fast moving'], 0, '“Frugal” means economical or careful about spending.'),
            ]),
        'science': lesson('Waves and reproduction',
            ['Waves transfer energy from place to place.', 'Reproduction allows living things to produce offspring.'],
            'Sound travels as vibrations through a medium such as air. In living things, reproduction passes genetic information from parent organisms to their offspring.', [
                question('What do waves transfer?', ['Energy', 'The medium itself over long distances', 'A new planet'], 0, 'Waves carry energy; the medium may vibrate locally.'),
                question('How does sound begin?', ['With vibrations', 'With a shadow', 'With a chemical formula'], 0, 'A vibrating source makes sound waves.'),
                question('What is an offspring?', ['A young organism produced by parents', 'A type of wave', 'A mineral'], 0, 'Offspring are the young produced through reproduction.'),
            ]),
    },
    9: {
        'maths': lesson('Indices, gradients, and equations',
            ['An index tells how many times to multiply a base by itself.', 'Gradient measures a line’s vertical change divided by its horizontal change.'],
            'Index laws help simplify repeated multiplication: 2³ × 2² is five factors of 2. On a straight-line graph, gradient describes how steeply the line rises or falls.', [
                question('What is 2³ × 2²?', ['2⁵ = 32', '2⁶ = 64', '4⁵ = 1,024'], 0, 'With the same base, add the powers: 2³ × 2² = 2⁵ = 32.'),
                question('What is the gradient between (1, 2) and (4, 8)?', ['1', '2', '6'], 1, 'Gradient = (8 - 2) ÷ (4 - 1) = 6 ÷ 3 = 2.'),
                question('Solve 2x - 5 = 9.', ['x = 2', 'x = 7', 'x = 14'], 1, 'Add 5 to get 2x = 14, then divide by 2.'),
            ]),
        'english': lesson('Symbolism and argument',
            ['Symbolism uses an object, place, or action to suggest a larger idea.', 'A clear argument gives a claim and supports it with reasons and evidence.'],
            'A locked gate in a story might symbolise a barrier or a missed opportunity. In an essay, a claim needs relevant evidence so the reader can understand why it matters.', [
                question('A character repeatedly sees a locked gate. What could it symbolise?', ['A barrier or limitation', 'A recipe', 'A weather report'], 0, 'A gate can suggest something that blocks progress.'),
                question('What should evidence do in an argument?', ['Support the claim', 'Replace every explanation', 'Confuse the reader'], 0, 'Evidence gives a reason to trust or consider the claim.'),
                question('Which is the clearest claim?', ['School gardens can support science learning.', 'Gardens.', 'Maybe something is good.'], 0, 'It states a specific position that can be supported.'),
            ]),
        'science': lesson('Atoms, elements, and energy transfer',
            ['Atoms are the building blocks of ordinary matter.', 'Energy can move between objects by heating, waves, or electrical transfer.'],
            'An element contains one kind of atom, such as oxygen or carbon. In a system, energy can be transferred without the energy simply vanishing.', [
                question('What does an element contain?', ['One kind of atom', 'Only water molecules', 'No particles'], 0, 'An element is made from one type of atom.'),
                question('Which is a common way energy transfers from a warm object to a cooler one?', ['Heating', 'Changing its name', 'Removing all atoms'], 0, 'Thermal energy can transfer from warmer to cooler places.'),
                question('What is the chemical symbol for oxygen?', ['O', 'Ox', 'Og'], 0, 'The symbol for oxygen is O.'),
            ]),
    },
    10: {
        'maths': lesson('Quadratics and right-angle trigonometry',
            ['A quadratic equation includes a squared variable.', 'Sine, cosine, and tangent relate angles to side lengths in right-angle triangles.'],
            'The equation x² = 9 has two solutions because both 3² and (-3)² equal 9. In a right-angle triangle, trigonometric ratios help find missing sides or angles.', [
                question('Solve x² = 9.', ['x = 3 only', 'x = -3 only', 'x = 3 or x = -3'], 2, 'Both 3² and (-3)² equal 9.'),
                question('What is sin(30°)?', ['0.5', '1', '2'], 0, 'The sine of 30 degrees is one half.'),
                question('What are the roots of x² - 4x + 3 = 0?', ['1 and 3', '-1 and -3', '0 and 4'], 0, 'Factor as (x - 1)(x - 3) = 0.'),
            ]),
        'english': lesson('Thesis, analysis, and allusion',
            ['A thesis states the main interpretation or argument of an essay.', 'An allusion refers to a known person, story, or event.'],
            'A strong analysis explains how a writer’s choices shape meaning. An allusion can add another layer when a writer refers to a familiar story or historical event.', [
                question('What does a thesis do?', ['States the essay’s central argument', 'Lists every source alphabetically', 'Repeats the question only'], 0, 'The thesis tells the reader the main position or interpretation.'),
                question('What is an allusion?', ['A reference to a familiar person, story, or event', 'A type of comma', 'A list of measurements'], 0, 'Allusions invite readers to connect a text with something they know.'),
                question('Which sentence analyses a writer’s choice?', ['The poem has four lines.', 'The repeated sea imagery makes the speaker’s worry feel constant.', 'I read the poem yesterday.'], 1, 'It explains an effect created by a language choice.'),
            ]),
        'science': lesson('Chemical reactions and inheritance',
            ['In a chemical reaction, atoms rearrange into new substances.', 'DNA carries inherited information in living things.'],
            'When iron rusts, iron atoms react with oxygen and form a new substance. In organisms, DNA stores instructions that can be passed from parents to offspring.', [
                question('What happens to atoms in a chemical reaction?', ['They are rearranged into new substances', 'They disappear', 'They become a different element every time'], 0, 'Chemical reactions rearrange atoms; they do not make atoms vanish.'),
                question('What does DNA carry?', ['Inherited biological information', 'Sound waves', 'Electric current only'], 0, 'DNA stores information used by living cells.'),
                question('Which is a sign that a new substance may have formed?', ['A lasting colour change', 'A shape drawn on paper', 'A number written down'], 0, 'A colour change can be evidence of a reaction, though context matters.'),
            ]),
    },
    11: {
        'maths': lesson('Functions, probability, and algebra',
            ['A function maps each allowed input to an output.', 'Expand brackets carefully and use probability values from 0 to 1.'],
            'For f(x) = 2x², substituting x = 3 gives f(3) = 2 × 3². A probability of 0.25 means an event has a one-in-four chance under the model.', [
                question('If f(x) = 2x², what is f(3)?', ['12', '18', '36'], 1, '2 × 3² = 2 × 9 = 18.'),
                question('What is the probability of two heads in two fair coin tosses?', ['1/2', '1/3', '1/4'], 2, 'The equally likely outcomes are HH, HT, TH, TT; only HH is two heads.'),
                question('Expand (x + 2)².', ['x² + 4', 'x² + 4x + 4', 'x² + 2x + 4'], 1, '(x + 2)(x + 2) = x² + 4x + 4.'),
            ]),
        'english': lesson('Close reading and supporting claims',
            ['Close reading looks carefully at words, structure, and patterns.', 'A strong analytical paragraph links evidence to an interpretation.'],
            'An image or repeated word can shape the mood of a text. When analysing it, explain the evidence and the effect it may have on a reader rather than just naming the technique.', [
                question('What is close reading?', ['Careful attention to language and structure', 'Reading only the title', 'Guessing without evidence'], 0, 'Close reading examines details and how they create meaning.'),
                question('What should follow a quotation in an analysis?', ['An explanation of its relevance', 'An unrelated fact', 'Another title only'], 0, 'Explain how the evidence supports your interpretation.'),
                question('Which word choice creates the most hopeful tone?', ['stalled', 'promising', 'bleak'], 1, '“Promising” suggests a positive possibility.'),
            ]),
        'science': lesson('Photosynthesis, genetics, and energy',
            ['Photosynthesis stores light energy in chemical energy in sugars.', 'Genes are sections of DNA that influence inherited traits.'],
            'Plants use light, water, and carbon dioxide to make sugars during photosynthesis. In living things, genes are parts of DNA that contribute to inherited characteristics.', [
                question('Which gas do plants take in for photosynthesis?', ['Carbon dioxide', 'Helium', 'Neon'], 0, 'Carbon dioxide is one of the raw materials for photosynthesis.'),
                question('What is a gene?', ['A section of DNA with biological information', 'A kind of wave', 'A whole ecosystem'], 0, 'Genes are segments of DNA that carry information.'),
                question('Where is energy stored after photosynthesis?', ['In chemical bonds of sugars', 'In the colour green only', 'In empty space'], 0, 'Photosynthesis converts light energy into chemical energy stored in sugars.'),
            ]),
    },
    12: {
        'maths': lesson('Calculus and data interpretation',
            ['A derivative describes an instantaneous rate of change.', 'Statistics helps describe data, but conclusions depend on how data was collected.'],
            'For y = x³, the derivative is 3x², which gives the slope at a chosen x-value. Data analysis also asks whether a sample is fair and whether a pattern is meaningful.', [
                question('For y = x³, what is the derivative at x = 2?', ['6', '8', '12'], 2, 'The derivative is 3x²; at x = 2 it is 3 × 4 = 12.'),
                question('What is the area under y = x from x = 0 to x = 4?', ['4', '8', '16'], 1, 'The region is a triangle with base 4 and height 4: ½ × 4 × 4 = 8.'),
                question('Why should a sample be representative?', ['So it fairly reflects the group being studied', 'So every answer is the same', 'So the graph has more colours'], 0, 'A representative sample reduces bias in conclusions.'),
            ]),
        'english': lesson('Comparative interpretation and synthesis',
            ['A comparative response explains meaningful similarities and differences.', 'Synthesis combines evidence from several sources to support one insight.'],
            'When comparing two texts, consider their contexts, voices, and choices of form. A strong response connects details from both texts to a clear interpretation rather than discussing them in isolation.', [
                question('What makes a comparison analytical?', ['It explains why similarities or differences matter', 'It lists titles only', 'It repeats one text twice'], 0, 'Analysis explains the significance of the comparison.'),
                question('What is synthesis?', ['Combining ideas and evidence into a new insight', 'Copying one source word for word', 'Sorting words by length'], 0, 'Synthesis connects information from multiple sources.'),
                question('Which thesis is most arguable?', ['Both texts use setting to show how belonging can change.', 'There are two texts.', 'One text has words.'], 0, 'It offers an interpretation that can be supported with evidence.'),
            ]),
        'science': lesson('Systems, evidence, and scientific models',
            ['Scientific models represent systems and can be revised when evidence improves.', 'A strong investigation uses suitable methods and considers uncertainty.'],
            'Models help scientists explain systems that are difficult to observe directly. New evidence can lead scientists to refine a model, while careful measurements help show how certain a conclusion should be.', [
                question('Why might scientists revise a model?', ['New evidence may explain the system better', 'Models can never change', 'A model is the same as a measurement'], 0, 'Models are updated when evidence or explanations improve.'),
                question('What does uncertainty describe in a measurement?', ['The range of doubt or variation around it', 'A guarantee that it is wrong', 'The colour of the equipment'], 0, 'Uncertainty shows the limits of precision in a measurement.'),
                question('Why repeat measurements?', ['To check consistency and reduce the effect of random variation', 'To make the result larger', 'To remove the need for a method'], 0, 'Repeated measurements help assess reliability and variation.'),
            ]),
    },
}

# Extra questions for every year and subject give each quiz a larger pool.
EXTRA_QUESTIONS = {
    1: {
        'maths': question('What is 5 + 2?', ['6', '7', '8'], 1, 'Five counters plus two more makes seven.'),
        'english': question('Which word starts with the same sound as “moon”?', ['map', 'sun', 'fish'], 0, '“Moon” and “map” both begin with the /m/ sound.'),
        'science': question('Which part of a plant takes in water from soil?', ['Roots', 'Flower petals', 'Fruit'], 0, 'Roots absorb water and anchor the plant.'),
    },
    2: {
        'maths': question('What is 50 + 9?', ['59', '509', '95'], 0, 'Five tens and nine ones make 59.'),
        'english': question('Which word names an action?', ['sleep', 'blue', 'chair'], 0, '“Sleep” is an action word, or verb.'),
        'science': question('Which material is attracted to a magnet?', ['Iron', 'Paper', 'Wood'], 0, 'Iron is a magnetic metal.'),
    },
    3: {
        'maths': question('There are 5 bags with 2 apples in each. How many apples?', ['7', '10', '12'], 1, 'Five groups of two make 5 × 2 = 10.'),
        'english': question('Which word describes how a bird sang?', ['sweetly', 'bird', 'sing'], 0, '“Sweetly” describes how the bird sang.'),
        'science': question('What is water called when it freezes?', ['Ice', 'Steam', 'Rain'], 0, 'Freezing changes liquid water into solid ice.'),
    },
    4: {
        'maths': question('What is one quarter of 20?', ['4', '5', '10'], 1, '20 divided into four equal parts gives 5 in each part.'),
        'english': question('Which detail is evidence that a character is tired?', ['They yawned and rubbed their eyes', 'They ran a race', 'They ate lunch'], 0, 'Yawning and rubbing eyes are clues of tiredness.'),
        'science': question('Which animal is a producer in a food chain?', ['Grass', 'Rabbit', 'Fox'], 0, 'Plants such as grass make their own food.'),
    },
    5: {
        'maths': question('What is 0.6 written as a fraction in tenths?', ['6/10', '6/100', '1/6'], 0, 'Six tenths is written 6/10.'),
        'english': question('Which sentence is written in the past tense?', ['Mia walked home.', 'Mia walks home.', 'Mia will walk home.'], 0, '“Walked” tells us the action already happened.'),
        'science': question('What is the main source of energy for Earth?', ['The Sun', 'The Moon', 'The ocean'], 0, 'Most energy for Earth’s systems comes from the Sun.'),
    },
    6: {
        'maths': question('A $40 item is discounted by 25%. What is the sale price?', ['$10', '$30', '$35'], 1, '25% of $40 is $10, so the sale price is $30.'),
        'english': question('What is the purpose of a topic sentence?', ['Introduce a paragraph’s main idea', 'List every source', 'Finish a whole book'], 0, 'A topic sentence signals the main idea of its paragraph.'),
        'science': question('Which change is reversible?', ['Ice melting', 'Wood burning', 'An egg cooking'], 0, 'Liquid water can be frozen again to make ice.'),
    },
    7: {
        'maths': question('Simplify the ratio 12:18.', ['2:3', '3:2', '6:9'], 0, 'Divide both parts by 6 to get 2:3.'),
        'english': question('What does a simile usually use to compare things?', ['Like or as', 'Because or so', 'Before or after'], 0, 'Similes compare using words such as “like” or “as”.'),
        'science': question('Which particle has a negative charge?', ['Electron', 'Proton', 'Neutron'], 0, 'Electrons carry a negative electrical charge.'),
    },
    8: {
        'maths': question('Solve x + 7 = 12.', ['x = 5', 'x = 19', 'x = -5'], 0, 'Subtract 7 from both sides: x = 5.'),
        'english': question('Which phrase best signals contrast?', ['On the other hand', 'For example', 'As a result'], 0, '“On the other hand” introduces a contrasting point.'),
        'science': question('What is the role of a decomposer?', ['Break down dead matter', 'Make sunlight', 'Stop all energy transfer'], 0, 'Decomposers recycle nutrients by breaking down dead matter.'),
    },
    9: {
        'maths': question('What is the gradient of y = 4x + 1?', ['1', '4', '5'], 1, 'In y = mx + b, the gradient is the coefficient m = 4.'),
        'english': question('What is an author’s tone?', ['Their attitude conveyed through the writing', 'The number of pages', 'The list of characters'], 0, 'Tone is the attitude or feeling conveyed by a text.'),
        'science': question('What is the unit of electrical current?', ['Ampere', 'Volt', 'Watt'], 0, 'Current is measured in amperes (amps).'),
    },
    10: {
        'maths': question('Factorise x² + 5x + 6.', ['(x + 2)(x + 3)', '(x + 1)(x + 6)', '(x - 2)(x - 3)'], 0, 'Two numbers that multiply to 6 and add to 5 are 2 and 3.'),
        'english': question('What makes a source useful as evidence?', ['It is relevant and trustworthy', 'It is the longest source', 'It agrees with every opinion'], 0, 'Relevant, reliable evidence helps support an argument.'),
        'science': question('What does a control variable do in an experiment?', ['Stay the same for a fair comparison', 'Change randomly', 'Replace the results'], 0, 'Keeping control variables constant helps isolate the tested factor.'),
    },
    11: {
        'maths': question('What is the mean of 2, 4, and 9?', ['5', '6', '15'], 0, 'The total is 15; divide by 3 values to get a mean of 5.'),
        'english': question('Why analyse the effect of a writer’s technique?', ['To explain how it shapes meaning or response', 'To count every word', 'To retell the plot only'], 0, 'Analysis connects a choice to its meaning or impact.'),
        'science': question('What does a catalyst do in a reaction?', ['Speeds it up without being used up', 'Stops all particles moving', 'Becomes the only product'], 0, 'A catalyst increases reaction rate and is not consumed overall.'),
    },
    12: {
        'maths': question('What is the derivative of x²?', ['x', '2x', '2'], 1, 'Using the power rule, d(x²)/dx = 2x.'),
        'english': question('What is the purpose of a counterargument?', ['Address a different or opposing view', 'Repeat the introduction', 'Add an unrelated detail'], 0, 'A counterargument recognises and responds to another position.'),
        'science': question('What does a larger sample size usually improve?', ['Reliability of an estimate', 'The certainty that bias is absent', 'The accuracy of every tool'], 0, 'A larger sample can reduce the effect of random variation.'),
    },
}

for year, subject_questions in EXTRA_QUESTIONS.items():
    for subject_slug, extra_question in subject_questions.items():
        YEAR_CONTENT[year][subject_slug]['questions'].append(extra_question)

# Four more level-specific questions per lesson. Answers are listed first here;
# the helper below moves them to a random position when building each bank.
MORE_QUESTIONS = {
    1: {
        'maths': [
            ('What is 3 + 4?', '7', '6', '8', 'Count on four from 3 to reach 7.'),
            ('Which number is greatest?', '9', '5', '7', 'Nine is greater than five and seven.'),
            ('There are 6 birds and 2 fly away. How many remain?', '4', '8', '3', 'Take 2 away from 6: 6 − 2 = 4.'),
            ('How many corners does a rectangle have?', '4', '3', '5', 'A rectangle has four corners.'),
        ],
        'english': [
            ('Which word begins with the letter B?', 'ball', 'sun', 'cat', 'Ball begins with B.'),
            ('Which word rhymes with “hop”?', 'mop', 'hot', 'hen', 'Hop and mop end with the same sound.'),
            ('Which is a question?', 'Where is my hat?', 'I found my hat.', 'My hat is red.', 'A question asks something and ends with a question mark.'),
            ('Which word names a person?', 'teacher', 'quickly', 'green', 'A teacher is a person.'),
        ],
        'science': [
            ('Which part of a plant is usually green and catches light?', 'Leaf', 'Root', 'Seed', 'Leaves catch light for the plant.'),
            ('Which animal lays eggs?', 'Hen', 'Cat', 'Dog', 'Hens lay eggs.'),
            ('What do we use to hear sounds?', 'Ears', 'Elbows', 'Knees', 'Our ears detect sounds.'),
            ('Which is a natural source of light?', 'The Sun', 'A book', 'A chair', 'The Sun gives out its own light.'),
        ],
    },
    2: {
        'maths': [
            ('What is 27 + 10?', '37', '28', '17', 'Adding one ten changes 27 to 37.'),
            ('What is 45 − 5?', '40', '50', '35', 'Five ones taken from 45 leaves 40.'),
            ('Which number has 3 tens and 8 ones?', '38', '83', '308', 'Three tens and eight ones make 38.'),
            ('How many sides does a hexagon have?', '6', '5', '8', 'A hexagon has six sides.'),
        ],
        'english': [
            ('Which is a describing word?', 'soft', 'run', 'table', '“Soft” describes how something feels.'),
            ('Which punctuation ends a question?', '?', '.', ',', 'A question mark signals a question.'),
            ('Which word means the opposite of “early”?', 'late', 'soon', 'first', 'Late is the opposite of early.'),
            ('Which word is plural?', 'dogs', 'dog', 'a dog', 'Dogs names more than one dog.'),
        ],
        'science': [
            ('Which material is flexible?', 'Rubber', 'Glass', 'Stone', 'Rubber can bend and stretch.'),
            ('What force pulls objects towards Earth?', 'Gravity', 'Sound', 'Light', 'Gravity pulls objects towards Earth.'),
            ('Which object is a source of heat?', 'A warm heater', 'An ice cube', 'A shadow', 'A heater transfers heat to its surroundings.'),
            ('What do most animals need to breathe?', 'Air', 'Sand', 'Plastic', 'Animals need gases in the air to breathe.'),
        ],
    },
    3: {
        'maths': [
            ('What is 6 × 4?', '24', '20', '10', 'Six groups of four make 24.'),
            ('What is 30 ÷ 5?', '6', '5', '25', 'Thirty shared into five equal groups gives six each.'),
            ('What is 100 − 37?', '63', '73', '67', 'Subtracting 37 from 100 gives 63.'),
            ('How many minutes are in half an hour?', '30', '15', '60', 'Half of 60 minutes is 30 minutes.'),
        ],
        'english': [
            ('Which word is an adverb in “The rabbit hopped quickly”?', 'quickly', 'rabbit', 'hopped', '“Quickly” tells how the rabbit hopped.'),
            ('Which sentence uses a comma in a list?', 'We saw birds, frogs, and fish.', 'We saw birds frogs and fish.', 'We, saw birds frogs and fish.', 'Commas separate items in a list.'),
            ('What is the setting of a story?', 'Where and when it happens', 'The title only', 'The final word', 'Setting tells the place and time.'),
            ('Which word is closest in meaning to “enormous”?', 'Huge', 'Tiny', 'Quiet', 'Enormous means very large.'),
        ],
        'science': [
            ('Which state of matter keeps its own shape?', 'Solid', 'Liquid', 'Gas', 'A solid keeps its shape unless a force changes it.'),
            ('What do we call an animal that eats plants?', 'Herbivore', 'Carnivore', 'Decomposer', 'Herbivores eat plants.'),
            ('Which part of a plant makes seeds?', 'Flower', 'Root', 'Stem only', 'Many plants produce seeds in flowers.'),
            ('What happens to a shadow when an object blocks light?', 'It forms behind the object', 'It makes its own light', 'It turns into sound', 'A shadow forms where light is blocked.'),
        ],
    },
    4: {
        'maths': [
            ('What is 3/8 + 2/8?', '5/8', '5/16', '1/8', 'With equal denominators, add the numerators: 3 + 2 = 5.'),
            ('What is 7 × 8?', '56', '54', '64', 'Seven groups of eight make 56.'),
            ('A rectangle is 5 cm long and 3 cm wide. What is its area?', '15 cm²', '16 cm²', '8 cm²', 'Area is length × width: 5 × 3 = 15 cm².'),
            ('What is 1,000 − 250?', '750', '850', '650', 'Taking 250 away from 1,000 leaves 750.'),
        ],
        'english': [
            ('Which word is a synonym for “brave”?', 'Courageous', 'Afraid', 'Careless', 'Courageous means brave.'),
            ('What does a pronoun replace?', 'A noun', 'A full paragraph', 'A punctuation mark', 'Pronouns such as “she” can stand in for a noun.'),
            ('Which sentence is direct speech?', '“I am ready,” said Sam.', 'Sam felt ready.', 'Sam was getting ready.', 'Direct speech shows the exact words spoken.'),
            ('Why might a writer use an exclamation mark?', 'To show strong feeling', 'To separate every noun', 'To start a paragraph', 'An exclamation mark can show excitement or emphasis.'),
        ],
        'science': [
            ('Which part of a food chain is usually the producer?', 'A green plant', 'A fox', 'A mushroom', 'Green plants make food using light.'),
            ('What is a force?', 'A push or a pull', 'A kind of habitat', 'A state of matter', 'Forces are pushes or pulls that can change motion.'),
            ('Which body system moves blood around the body?', 'Circulatory system', 'Digestive system', 'Skeletal system', 'The circulatory system transports blood.'),
            ('What is condensation?', 'Gas changing into liquid', 'Solid changing into gas', 'Liquid changing into solid', 'Cooling water vapour can condense into liquid droplets.'),
        ],
    },
    5: {
        'maths': [
            ('What is 3.7 + 1.8?', '5.5', '4.15', '5.15', 'Align decimal points: 3.7 + 1.8 = 5.5.'),
            ('What is 2/3 of 18?', '12', '9', '6', 'One third of 18 is 6, so two thirds is 12.'),
            ('What is the volume of a 2 × 3 × 4 cm box?', '24 cm³', '9 cm³', '24 cm²', 'Volume is length × width × height: 2 × 3 × 4 = 24 cm³.'),
            ('Which is a prime number?', '13', '15', '21', '13 has exactly two factors: 1 and 13.'),
        ],
        'english': [
            ('Which connective shows cause?', 'because', 'meanwhile', 'although', '“Because” introduces a reason.'),
            ('What is the first-person pronoun in “We explored the cave”?', 'We', 'explored', 'cave', '“We” is a first-person pronoun.'),
            ('What is a character’s motivation?', 'The reason for their actions', 'The book’s page count', 'The story’s setting', 'Motivation explains why a character acts.'),
            ('Which word is an antonym of “ancient”?', 'Modern', 'Old', 'Historic', 'Modern is the opposite of ancient.'),
        ],
        'science': [
            ('Which organ pumps blood?', 'Heart', 'Lung', 'Stomach', 'The heart pumps blood through the body.'),
            ('What is the variable you deliberately change called?', 'Independent variable', 'Dependent variable', 'Control variable', 'The independent variable is the factor changed by the investigator.'),
            ('Which is a renewable energy source?', 'Wind', 'Coal', 'Petrol', 'Wind is naturally replenished.'),
            ('What causes day and night?', 'Earth rotating on its axis', 'The Moon orbiting Earth', 'The Sun orbiting Earth each day', 'Earth’s rotation brings places into and out of sunlight.'),
        ],
    },
    6: {
        'maths': [
            ('What is 3/5 + 1/10?', '7/10', '4/15', '4/10', 'Convert 3/5 to 6/10, then add 1/10.'),
            ('What is 15% of 80?', '12', '8', '15', '10% is 8 and 5% is 4, so 15% is 12.'),
            ('What is the mean of 4, 6, and 8?', '6', '18', '7', 'Add to get 18, then divide by 3.'),
            ('A triangle has angles 50° and 60°. What is the third angle?', '70°', '80°', '90°', 'Triangle angles total 180°; 180 − 50 − 60 = 70°.'),
        ],
        'english': [
            ('Which is a complex sentence?', 'Although it rained, we played.', 'It rained.', 'Rain fell; clouds gathered.', '“Although” introduces a dependent clause.'),
            ('What is the purpose of a persuasive text?', 'To convince the reader', 'To list random facts', 'To give stage directions', 'Persuasive writing aims to influence an audience.'),
            ('Which phrase uses personification?', 'The wind whispered', 'The wind was strong', 'The wind from the south', 'Whispering is a human action given to the wind.'),
            ('What does “reluctant” mean?', 'Unwilling', 'Eager', 'Certain', 'A reluctant person is not keen to do something.'),
        ],
        'science': [
            ('Which process lets liquid water enter the air as water vapour?', 'Evaporation', 'Condensation', 'Freezing', 'Evaporation changes liquid water into water vapour.'),
            ('What is the main job of the lungs?', 'Exchange gases', 'Pump blood', 'Digest food', 'The lungs take in oxygen and release carbon dioxide.'),
            ('What is a fair test?', 'One that changes one factor at a time', 'One with no measurements', 'One where results are chosen first', 'Changing one factor helps identify its effect.'),
            ('Which object is a good electrical insulator?', 'Rubber', 'Copper', 'Aluminium', 'Rubber resists the flow of electric current.'),
        ],
    },
    7: {
        'maths': [
            ('What is −6 + 10?', '4', '-16', '16', 'Moving ten places right from −6 lands on 4.'),
            ('What is 0.25 as a percentage?', '25%', '2.5%', '250%', 'Multiply 0.25 by 100 to get 25%.'),
            ('A map scale is 1 cm to 5 km. What distance is 4 cm?', '20 km', '9 km', '25 km', 'Four centimetres represent 4 × 5 = 20 km.'),
            ('What is the value of 3² + 4?', '13', '49', '10', 'Evaluate the power first: 9 + 4 = 13.'),
        ],
        'english': [
            ('What is the narrator?', 'The voice telling the story', 'The story’s setting', 'The book cover', 'The narrator is the voice or perspective through which a story is told.'),
            ('Which is an example of alliteration?', 'Wild winds whistle', 'The wind was cold', 'A quiet afternoon', 'The repeated initial w sound creates alliteration.'),
            ('What is the purpose of a headline?', 'To introduce and attract interest in a story', 'To provide the ending', 'To list every source', 'A headline summarises or draws attention to a story.'),
            ('Which modal verb suggests possibility?', 'might', 'must', 'will', '“Might” expresses possibility rather than certainty.'),
        ],
        'science': [
            ('What is the centre of an atom called?', 'Nucleus', 'Cell wall', 'Circuit', 'The nucleus contains protons and neutrons.'),
            ('Which variable is measured as the outcome?', 'Dependent variable', 'Independent variable', 'Control variable', 'The dependent variable responds to the change being tested.'),
            ('What is an adaptation?', 'A feature that helps an organism survive', 'A sudden weather event', 'A kind of rock', 'Adaptations can help organisms meet challenges in their environment.'),
            ('Which planet is closest to the Sun?', 'Mercury', 'Venus', 'Mars', 'Mercury is the innermost planet in our Solar System.'),
        ],
    },
    8: {
        'maths': [
            ('Expand 2(x + 5).', '2x + 10', '2x + 5', 'x + 10', 'Multiply both terms inside the brackets by 2.'),
            ('What is the area of a circle with radius 2?', '4π', '2π', '8π', 'Area = πr² = π × 2² = 4π.'),
            ('What is the probability of rolling an even number on a fair six-sided die?', '1/2', '1/3', '2/3', 'Three of the six outcomes are even, so 3/6 = 1/2.'),
            ('Solve 5x = 35.', 'x = 7', 'x = 30', 'x = 40', 'Divide both sides by 5.'),
        ],
        'english': [
            ('What is a rhetorical question?', 'A question asked for effect', 'A question with no question mark', 'A list of facts', 'Rhetorical questions prompt thought without requiring an answer.'),
            ('Which sentence is in the passive voice?', 'The match was won by our team.', 'Our team won the match.', 'Our team is winning.', 'The subject “match” receives the action.'),
            ('What is connotation?', 'The associations a word suggests', 'Its number of syllables', 'Its place in a sentence', 'Connotation refers to feelings or ideas associated with a word.'),
            ('Which connective signals a conclusion?', 'therefore', 'however', 'for instance', '“Therefore” signals a result or conclusion.'),
        ],
        'science': [
            ('What is the chemical formula for water?', 'H₂O', 'CO₂', 'O₂', 'A water molecule contains two hydrogen atoms and one oxygen atom.'),
            ('What is the function of a cell membrane?', 'Control what enters and leaves the cell', 'Store all genetic information', 'Make bones', 'The membrane regulates movement into and out of a cell.'),
            ('What is the unit of force?', 'Newton', 'Joule', 'Watt', 'Force is measured in newtons.'),
            ('What happens to particles when a substance is heated?', 'They gain energy and move more', 'They stop moving', 'They disappear', 'Heating usually increases particle motion.'),
        ],
    },
    9: {
        'maths': [
            ('Solve 2x + 3 = 11.', 'x = 4', 'x = 7', 'x = 14', 'Subtract 3, then divide 8 by 2.'),
            ('What is the gradient of a horizontal line?', '0', '1', 'Undefined', 'A horizontal line has no vertical change, so its gradient is zero.'),
            ('What is the circumference of a circle with diameter 6?', '6π', '12π', '3π', 'Circumference = πd = 6π.'),
            ('If a = 3 and b = 2, what is a² − b?', '7', '5', '14', 'Substitute: 3² − 2 = 9 − 2 = 7.'),
        ],
        'english': [
            ('What is an extended metaphor?', 'A metaphor developed across a text', 'A comparison using “like” once', 'A factual description', 'An extended metaphor continues a comparison over several lines or ideas.'),
            ('What does a cohesive device do?', 'Links ideas across a text', 'Changes the text’s font', 'Names the audience', 'Cohesive devices help ideas connect smoothly.'),
            ('What is bias in a source?', 'A partial perspective that may affect presentation', 'A measurement unit', 'A type of paragraph', 'Bias can shape which facts or viewpoints are emphasised.'),
            ('Which phrase gives a qualified claim?', 'In some cases', 'Without a doubt, always', 'Everyone knows', '“In some cases” limits a claim rather than making it absolute.'),
        ],
        'science': [
            ('What is the charge of a proton?', 'Positive', 'Negative', 'Neutral', 'Protons carry a positive charge.'),
            ('What is the purpose of a fuse?', 'Break a circuit if current is too high', 'Increase the voltage', 'Store chemical energy', 'A fuse melts and opens the circuit when excessive current flows.'),
            ('Which type of rock forms from cooled magma or lava?', 'Igneous', 'Sedimentary', 'Metamorphic', 'Igneous rock forms when molten rock cools and solidifies.'),
            ('What is biodiversity?', 'The variety of living things', 'The speed of a planet', 'The amount of rainfall only', 'Biodiversity describes the variety of organisms in an area.'),
        ],
    },
    10: {
        'maths': [
            ('What is the solution to x² = 16?', 'x = 4 or x = −4', 'x = 8 only', 'x = −8 only', 'Both 4² and (−4)² equal 16.'),
            ('What is sin(90°)?', '1', '0', '−1', 'The sine of 90 degrees is 1.'),
            ('A $50 price increases by 10%. What is the new price?', '$55', '$60', '$45', '10% of $50 is $5, so the new price is $55.'),
            ('What is the midpoint of (2, 4) and (6, 8)?', '(4, 6)', '(8, 12)', '(2, 2)', 'Average the x-coordinates and y-coordinates separately.'),
        ],
        'english': [
            ('What is the purpose of a bibliography?', 'List the sources used', 'Introduce the main character', 'Summarise each paragraph', 'A bibliography acknowledges and lists sources.'),
            ('What does juxtaposition do?', 'Places ideas side by side to highlight contrast', 'Repeats a rhyme scheme', 'Removes the text’s context', 'Juxtaposition invites readers to compare nearby ideas.'),
            ('What is a reliable primary source?', 'A firsthand record relevant to the topic', 'An unrelated opinion copied online', 'A fictional summary', 'Primary sources provide direct or firsthand evidence.'),
            ('What is the effect of using a short sentence after a long one?', 'It can create emphasis or a pause', 'It always changes the tense', 'It removes the subject', 'A short sentence can make a point feel sharp or emphatic.'),
        ],
        'science': [
            ('What is the pH of a neutral solution at room temperature?', '7', '0', '14', 'A neutral solution has pH 7.'),
            ('What is the role of DNA in a cell?', 'Store genetic instructions', 'Carry oxygen in blood', 'Digest food', 'DNA stores instructions used in cell functions and inheritance.'),
            ('What is the acceleration of an object at constant velocity?', '0', 'Equal to its speed', 'Always increasing', 'Constant velocity means velocity is not changing.'),
            ('Which gas is released by plants during photosynthesis?', 'Oxygen', 'Nitrogen', 'Methane', 'Oxygen is produced during photosynthesis.'),
        ],
    },
    11: {
        'maths': [
            ('What is the gradient of y = 3x − 2?', '3', '-2', '1', 'The coefficient of x gives the gradient.'),
            ('What is the probability of rolling a number greater than 4 on a fair die?', '1/3', '1/2', '2/3', 'The outcomes are 5 and 6: 2/6 = 1/3.'),
            ('Simplify (x³)(x²).', 'x⁵', 'x⁶', '2x⁵', 'When multiplying powers with the same base, add exponents.'),
            ('What is the median of 2, 3, 8, 10, 12?', '8', '3', '7', 'The median is the middle value in the ordered list.'),
        ],
        'english': [
            ('What is an unreliable narrator?', 'A narrator whose account may not be fully trusted', 'A narrator who speaks in rhyme', 'A character with no dialogue', 'An unreliable narrator may omit, misunderstand, or distort events.'),
            ('What is an imperative sentence used for?', 'Giving a command or instruction', 'Asking a question only', 'Reporting past events only', 'Imperatives tell someone to do something.'),
            ('What does textual context include?', 'Relevant circumstances around a text', 'Only the final sentence', 'The font size', 'Context can include time, place, audience, and purpose.'),
            ('Which phrase signals a concession?', 'Admittedly', 'For example', 'As a result', '“Admittedly” acknowledges a point before qualifying an argument.'),
        ],
        'science': [
            ('What is the SI unit of energy?', 'Joule', 'Newton', 'Ampere', 'Energy is measured in joules.'),
            ('What does natural selection act on?', 'Inherited variation affecting survival and reproduction', 'Traits acquired in one day', 'Random choices by organisms', 'Natural selection changes populations through heritable differences.'),
            ('What is the independent variable in an investigation?', 'The factor deliberately changed', 'The measured result', 'A factor kept constant', 'The independent variable is the one the investigator changes.'),
            ('What does a half-life describe?', 'Time for half of a radioactive sample to decay', 'Time for a planet to orbit twice', 'The mass of a single atom', 'Half-life is the time for half the unstable nuclei to decay.'),
        ],
    },
    12: {
        'maths': [
            ('What is the derivative of 3x²?', '6x', '3x', '6', 'Apply the power rule: 3 × 2x = 6x.'),
            ('What is ∫ 2x dx?', 'x² + C', '2 + C', '2x² + C', 'An antiderivative of 2x is x²; include the constant C.'),
            ('If two events are independent, how do you find P(A and B)?', 'P(A) × P(B)', 'P(A) + P(B)', 'P(A) − P(B)', 'For independent events, multiply their probabilities.'),
            ('What does a 95% confidence interval describe?', 'A range produced by a method with stated long-run coverage', 'A guarantee that one result is correct', 'The largest possible sample', 'The interval method has 95% coverage over repeated samples under its assumptions.'),
        ],
        'english': [
            ('What is an intertextual reference?', 'A connection to another text', 'A list of chapter titles', 'A sentence without a verb', 'Intertextuality links one text with another.'),
            ('What is a discourse community?', 'A group that shares communication practices and purposes', 'A list of unrelated readers', 'A type of rhyme', 'Discourse communities share conventions for communicating.'),
            ('What does register refer to?', 'Language choices suited to a context', 'The order of a bibliography', 'The number of characters', 'Register shifts with audience, purpose, and situation.'),
            ('What is the purpose of a synthesis paragraph?', 'Combine sources to develop an insight', 'Summarise one source only', 'Add evidence without linking it', 'Synthesis connects evidence from multiple sources into a reasoned point.'),
        ],
        'science': [
            ('What does the slope of a displacement-time graph represent?', 'Velocity', 'Acceleration', 'Force', 'The change in displacement per unit time is velocity.'),
            ('What is a confidence level in statistical inference?', 'A long-run success rate of the interval procedure', 'The probability a hypothesis is true', 'The size of the population', 'Confidence describes the method’s long-run interval coverage.'),
            ('What is an isotope?', 'Atoms of the same element with different neutron numbers', 'Atoms with different proton numbers but same name', 'A molecule with no electrons', 'Isotopes share proton number but differ in neutron number.'),
            ('What is a limitation of a scientific model?', 'It simplifies aspects of the real system', 'It always contains every detail', 'It cannot be revised', 'Models are useful simplifications and may not capture every detail.'),
        ],
    },
}

def build_question_bank_entry(prompt, correct, wrong_one, wrong_two, explanation):
    options = [correct, wrong_one, wrong_two]
    random.shuffle(options)
    return question(prompt, options, options.index(correct), explanation)


for year, subject_questions in MORE_QUESTIONS.items():
    for subject_slug, entries in subject_questions.items():
        YEAR_CONTENT[year][subject_slug]['questions'].extend(
            build_question_bank_entry(*entry) for entry in entries
        )


def year_band(year):
    if year <= 6:
        return 'Primary years'
    if year <= 10:
        return 'Secondary years'
    return 'Senior secondary years'
