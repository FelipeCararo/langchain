from langchain_openai import ChatOpenAI
from langchain_text_splitters import RecursiveCharacterTextSplitter
from langchain_core.prompts import ChatPromptTemplate
from dotenv import load_dotenv
load_dotenv()

long_text = """
Dawn threads a pale gold through the alley of glass.
The city yawns in a chorus of brakes and distant sirens.
Windows blink awake, one by one, like sleepy eyes.
Streetcloth of steam curls from manholes, a quiet river.
Coffee steam spirals above a newspaper's pale print.
Pedestrians sketch light on sidewalks, hurried, loud with umbrellas.
Buses swallow the morning with their loud yawns.
A sparrow perches on a steel beam, surveying the grid.
The subway sighs somewhere underground, a heartbeat rising.
Neon still glows in the corners where night refused to retire.
A cyclist cuts through the chorus, bright with chrome and momentum.
The city clears its throat, the air turning a little less electric.
Shoes hiss on concrete, a thousand small verbs of arriving.
Dawn keeps its promises in the quiet rhythm of a waking metropolis.
The morning light cascades through towering windows of steel and glass,
casting geometric shadows on busy streets below.
Traffic flows like rivers of metal and light,
while pedestrians weave through crosswalks with purpose.
Coffee shops exhale warmth and the aroma of fresh bread,
as commuters clutch their cups like talismans against the cold.
Street vendors call out in a symphony of languages,
their voices mixing with the distant hum of construction.
Pigeons dance between the feet of hurried workers,
finding crumbs of breakfast pastries on concrete sidewalks.
The city breathes in rhythm with a million heartbeats,
each person carrying dreams and deadlines in equal measure.
Skyscrapers reach toward clouds that drift like cotton,
while far below, subway trains rumble through tunnels.
This urban orchestra plays from dawn until dusk,
a endless song of ambition, struggle, and hope.
"""

splitter = RecursiveCharacterTextSplitter(
    chunk_size=250, chunk_overlap=70,
)

parts = splitter.create_documents([long_text])

# for part in parts:
#     print(part.page_content)
#     print("-"*30)

llm = ChatOpenAI(model="gpt-5-nano", temperature=0)

# Map step: summarize each chunk individually
map_prompt = ChatPromptTemplate.from_messages([
    ("system", "You are a helpful assistant that summarizes text concisely."),
    ("user", "Summarize the following text:\n\n{text}"),
])
map_chain = map_prompt | llm

print("--- MAP STEP ---")
summaries = []
for part in parts:
    result = map_chain.invoke({"text": part.page_content})
    print(f"Chunk summary: {result.content}")
    summaries.append(result.content)

# Reduce step: combine all summaries into a final one
reduce_prompt = ChatPromptTemplate.from_messages([
    ("system", "You are a helpful assistant that combines multiple summaries into one final concise summary."),
    ("user", "Combine the following summaries into a single final summary:\n\n{text}"),
])
reduce_chain = reduce_prompt | llm

print("\n--- REDUCE STEP ---")
combined = "\n\n".join(summaries)
final_result = reduce_chain.invoke({"text": combined})
print(f"Final summary: {final_result.content}")
