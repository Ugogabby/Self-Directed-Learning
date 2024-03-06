import streamlit as st

st.set_page_config(
    page_title="Developing Moral Resilience through Forgiveness",
    page_icon="random",
    layout="wide",
    initial_sidebar_state="expanded",
    menu_items={'About': "Learn to be More Forgiving in Less Than Two Hours!"}
)


st.image('VETERAN_Lab_Logo.png', width=400, use_column_width="never", clamp=False, channels="RGB", output_format="auto")


st.title('Developing Moral Resilience through Forgiveness')
st.header(
    """ :blue[Learn to be More Forgiving in Less Than Two Hours]
    """
    )
st.subheader(
    """Self-Directed Learning 
    Exercises to Build Forgiveness
    """
)
st.markdown(
    """ 
    <p style="text-align: center;"><span style="color:Orange;font-weight:bold;">Justin McDaniel, PhD</span>
    <p style="text-align: center;"><span style="color:violet;font-weight:bold;">Southern Illinois University</span>

    """, unsafe_allow_html=True
)

st.divider()
st.markdown(
        """ 
        ## :blue[Lesson 1]
        What is this workbook all about?
        
        <p style="text-align: center;">Introduction to the <span style="color:green;font-weight:bold;">BREACH/PREACH</span> Forgiveness Workbook
       """, unsafe_allow_html=True
)


acronyms = [
    "B/P - Betrayal or Perpetration-Based Moral Injury Knowledge",
    "R - Recall the Hurt",
    "E - Empathizing with the Wrongdoer or Yourself",
    "A - Altruistic Gift of Forgiveness",
    "C - Committing to the Forgiveness You've Experienced",
    "H - Holding onto Forgiveness in Times of Doubt"
]

for item in acronyms:
    st.markdown(f"<b>{item[0]}</b>{item[1:]}", unsafe_allow_html=True)



st.write(
    """
Within a span of less than two hours, engage in practical exercises aimed at fostering forgiveness, which can aid in reconciling choices and actions that conflict with one's values. Forgiveness is a voluntary act; no one is obligated to forgive.

Contained within this guide are twelve ten-minute exercises, totaling approximately two hours for completion. These exercises progressively build upon one another, so it's advised not to skip any. Each exercise is brief, allowing for easy integration into your daily routine. By participating in these exercises, you have the opportunity to develop what we’ll call “moral resilience.”

Forgiveness can yield swift and profound results, potentially altering your life's trajectory. However, more often, it instigates subtle yet significant shifts in direction. These changes, though seemingly minor, lead you toward a different destination than your current path. Whether a sudden transformation or gradual evolution, forgiveness guides you toward a brighter future, helping you come to terms with choices and actions that you have made that may conflict with your value system.

Crucially, forgiveness does not entail forgetting or denying past hurts. Rather, it involves replacing animosity with benevolence towards the wrongdoer or yourself. Furthermore, forgiveness doesn't preclude seeking justice; it entails desiring the offender's ultimate well-being while pursuing a fair resolution. Embracing forgiveness can be a transformative and liberating experience. Let's embark on this journey of forgiveness together.
""")

st.header(
        """ :blue[Exercise 1.1]
        Rating Your Typical Use of Forgiveness
       """
)

st.write(
    """Reflect on your past experience with forgiveness, encompassing interactions with all individuals you've encountered and the various hurts 
    you've endured personally – even based on your own actions. If you perceive yourself as consistently forgiving in nearly all 
    circumstances with virtually everyone you've encountered, assign yourself a score of 10, indicating complete forgiveness. Conversely, 
    if you find that you frequently experience anger, hurt, resentment, guilt, shame, or bitterness when faced with unfair treatment or 
    emotional injury, assign yourself a score of zero. Provide an honest assessment of your current life situation. 
    """
)
with st.form("rating_1"):
    col1, col2 = st.columns(2)
    col1.write("How forgiving are you as a person, from 0 (not at all) to 10 (completely)?")
    role_res = col2.radio('Pick one:', [1, 2, 3, 4, 5, 6, 7, 8, 9, 10], index=None, horizontal=True, key=1.1)
    submitted = st.form_submit_button("Submit")


st.header(
        """ :blue[Exercise 1.2]
        Moral Injury and Choosing a Hurt You Want to Work to Forgive
       """
)
st.write(
    """Moral injury refers to the psychological and emotional distress experienced when an individual witnesses or participates in actions that violate their moral or ethical beliefs, especially in the context of military service and combat. For military personnel and veterans, moral injury often occurs when they are confronted with situations where they perceive themselves or others as having transgressed deeply held moral principles, such as killing innocent civilians, witnessing or participating in atrocities, experiencing betrayal from trusted colleagues, or failing to prevent harm to fellow service members.
Unlike traditional definitions of trauma, moral injury focuses on the internal conflict arising from actions that are perceived as morally wrong, rather than solely on the external events themselves. This internal conflict can lead to feelings of guilt, shame, anger, and spiritual or existential distress. Moral injury can significantly impact an individual's mental health, leading to conditions such as depression, substance use, and suicidal ideation.
One aspect of forgiveness revolves around your response to a specific moral injury. Some individuals believe, "I've experienced such profound pain that forgiveness is impossible." This notion is unfounded. Even the most severe injuries can be forgiven, albeit challenging. Becoming a more forgiving individual entails forgiving one injury at a time. Therefore, select an injury that presently seems unforgivable. Transport yourself back to the moment of the injury; chances are, you can still recall the pain vividly. Events may have unfolded since then, exacerbating the pain. Perhaps the individual responsible never apologized or you never acknowledged your own wrongdoing. Alternatively, they may have inflicted further harm or betrayed you since then. This injury is the focal point for your efforts in this workbook. It could serve as the initial stride toward cultivating a lifestyle of moral resilience and greater forgiveness within yourself. 

"""
)

with st.form("injury_1.2"):
    col1, col2 = st.columns(2)
    col1.write("Write a brief description of the injury to reaffirm your commitment to forgiving this specific offense. Enter your description below.")
    role_res = col2.text_area("", placeholder="Enter your description here", key=1.2, max_chars=2000)
    
    st.write(
    """Throughout these 12 exercises, you will address this specific injury. Your objective is to achieve complete forgiveness by the conclusion. It's possible that for a significant injury, complete forgiveness may not be immediate, but significant progress will be made (and you may even surprise yourself!). You can revisit this workbook until you have fully forgiven the injury. Pursuing forgiveness is akin to medication for an ailment causing a fever; the initial dose may alleviate the symptoms, but recurrence is possible. Multiple doses may be necessary until the ailment is eradicated. Towards the conclusion of these sessions, you will contemplate other injuries and practice forgiveness, further fostering your journey towards becoming a more forgiving individual and a military service member or veteran who is morally resilient.
"""
)
    submitted = st.form_submit_button("Submit")
    

st.header(
        """ :blue[Exercise 1.3]
        How Willing are you to Forgive Right Now?
       """
)
st.write(
    """Unforgiveness manifests when one harbors a reluctance to grant forgiveness. Moving towards forgiveness entails traversing two distinct phases. Firstly, there's the conscious decision regarding how to regard yourself or approach another individual in the future. A true act of forgiveness involves opting not to retaliate in kind for any inflicted pain but instead opting to regard oneself or the other person with appreciation. Let's denote this as a 10 on the forgiveness scale. Conversely, if the inclination is towards revenge, avoidance of the problem or individual, or exacerbating the harm inflicted upon oneself or another, then genuine forgiveness is absent, registering at a 0 on the scale. 
"""
)

with st.form("willing_1.3"):
    col1, col2 = st.columns(2)
    col1.write("Assess your current state in the journey towards forgiveness by rating yourself from 0 (no progress) to 10 (complete forgiveness).")
    role_res = col2.radio('Pick your rating here:', [1, 2, 3, 4, 5, 6, 7, 8, 9, 10], index=None, horizontal=True, key=1.3)

    submitted = st.form_submit_button("Submit")

st.header(
        """ :blue[Exercise 1.4]
        Rating your Emotional Forgiveness
       """
)
st.write(
    """Even if you've genuinely resolved to forgive, it's still possible to grapple with lingering feelings of resentment, bitterness, anger, shame, guilt, and apprehension about future hurt. Hatred towards yourself or another individual who caused you pain might even persist. There exists another facet of forgiveness known as emotional forgiveness. Emotional forgiveness entails substituting negative, unforgiving emotions with more positive sentiments directed towards the wrongdoer. Let's gauge your level of emotional forgiveness. If you find yourself engulfed in intense negative emotions without a hint of forgiveness, assign yourself a rating of 0. If you harbor no negativity whatsoever towards yourself or the individual, give yourself a score of 10.
Consider the dynamics of your relationship with the person who inflicted harm upon you, or the dynamics of the situation that you might have perpetrated/witnessed. Achieving complete emotional forgiveness in a context that you will never have to engage with again involves purging yourself of all negative emotions like hatred or bitterness towards another person or yourself. However, if the hurt stems from a situation that you will encounter again or a person you will see again—such as a romantic partner, child, parent, close friend, or a place/circumstance that you will be in again—attaining full emotional forgiveness necessitates more than just relinquishing negative feelings: you must also cultivate positive emotions like love towards another person, or you must reflect on a circumstance and reconcile it with your value system in order to move forward in a way that leaves you confident in your decision making.
Given that you've chosen to confront this significant hurt, your current rating might lean towards the lower end. Nonetheless, your journey towards emotional forgiveness will evolve positively as you progress through the 12 prescribed exercises.

"""
)

with st.form("emotions_1.4"):
    col1, col2 = st.columns(2)
    col1.write("If you find yourself engulfed in intense negative emotions without a hint of forgiveness, assign yourself a rating of 0. If you harbor no negativity whatsoever towards yourself or the individual, give yourself a score of 10.")
    role_res = col2.radio('Pick your rating here:', [1, 2, 3, 4, 5, 6, 7, 8, 9, 10], index=None, horizontal=True, key=1.4)

    submitted = st.form_submit_button("Submit")

st.header(
        """ :blue[Exercise 1.5]
        Rating your Emotional Forgiveness
       """
)
st.write(
    """Once you complete a lesson, you will be presented with a review of material and a small test to ensure that you are engaging with the context carefully. 
    In lesson one, you learned a lot about moral injury and forgiveness as a way to build moral resilience. You’ve learned that 

•	Moral injury refers to the psychological and emotional distress experienced when an individual witnesses or participates in actions that violate their moral or ethical beliefs, especially in the context of military service and combat.

•	Forgiveness may be classified into two types: forgiveness as a general practice and using forgiveness to reconcile a particular hurt.

•	Forgiving a hurt may take place in two ways.  

"""
)

with st.form("forgive_1.5"):
    st.text_input(
    """You first must make a ***d***____ to forgive. Secondly, you may experience ***e***_____ forgiveness. Did you recall these two types of forgiveness?""", placeholder='E______  and F______')
    submitted = st.form_submit_button("Submit")


st.header(
        """ :blue[lesson 2]
        Why should you forgive?
       """
)
st.write(
    """This lesson might require more time than the usual 10 minutes due to its critical nature. You'll dive into the reasons behind your desire to extend forgiveness to yourself for your own actions/experiences or the individual who caused you harm.
    """
)

st.header(
        """ :blue[lesson 2.1]
        Literature as a Basis for Learning about Forgiveness
       """
)

with st.form("Literature_2.1"):
    st.write(
    """Quote 1: It may be helpful to think about what other people have said about forgiveness. :blue[Maya Angelou], who was an American poet, wrote the following:
History, despite its wrenching pain,
Cannot be unlived, but if faced with courage
Need not be lived again.
"""
)

    st.text_input(" :green[If you were to select just one word that resonates most strongly with you from this quote, what would it be?]")
    
    st.write(" :blue[Read the quote again and answer the two questions presented below.]")
    st.text_input(" :green[Is the quote meaningful to you? Type Yes or No below:]")
    st.text_area(" :green[Why or why not? Type your reasons below:]")
    st.write(
    """Quote 2: The following is a :blue[Malachy McCourt] quote (writer, actor, and politician):
Resentment is like taking poison and waiting for the other person to die.
"""
)
    st.text_area(" :green[Can you rephrase this quote below?]")
    st.write(
    """One possible way to rephrase this quote follows: “holding on to unforgiveness doesn’t hurt the person who injured you, but it is bad for you.” There is support from many scientific studies that this is true.
"""
)
    submitted = st.form_submit_button("Submit")




st.header(
        """ :blue[Exercise 2.2]
        What are the benefits of forgiveness?
       """
)
st.write(
    """Many individuals view unforgiveness and seeking revenge as valid options instead of forgiveness. Why bear the weight of a grudge or mistake that breeds anger, physical ailments, and disrupts spiritual harmony? Numerous scientifically endorsed advantages accompany the act of forgiveness, both in terms of decision-making and emotional well-being. List as many benefits of embracing forgiveness as possible, spanning physical health, mental well-being, interpersonal relationships, and any other facets of life, such as spirituality. Your gains will be maximized by striving to compile an extensive list before proceeding to Exercise 2.3"""
)
with st.form("benefits_2.2"):
   st.text_area("Benefits for Physical Health:", placeholder="Type here", key=2.21, max_chars=2000)
   st.text_area("Benefits for Mental Health:", placeholder="Type here", key=2.22, max_chars=2000)
   st.text_area("Benefits for Relationships:", placeholder="Type here", key=2.23, max_chars=2000)
   st.text_area("Benefits for Spirituality:", placeholder="Type here", key=2.24, max_chars=2000)

   submitted = st.form_submit_button("Submit")

st.header(
        """ :blue[Exercise 2.3]
        Scientific Benefits of Forgiveness
       """
)
st.write(
    """Below are scientifically validated outcomes of forgiveness. Read these.

1.	Clinging to resentments proves to be a source of stress, triggering an increase in cortisol levels within the body. Cortisol is released when you are stressed and it can have disastrous effects in your body if it is chronic. It elevates blood pressure, heart rate, and the likelihood of cardiac issues. Additionally, it can manifest in digestive complications, a weakened immune system, diminished libido, and impaired memory. (How many considerations did you anticipate in advance?)
2.	Nursing grudges or resentments induces feelings of depression, anxiety over potential future harm, anger, and a general shift towards negativity. Individuals often find themselves fixating on the adverse event and its repercussions, perpetuating emotional distress. These negative emotions inevitably take a toll on one's physical well-being.
3.	Maintaining grudges impedes the desire for reconciliation in relationships. It fosters lingering anger, emotional detachment from the other party, and bitterness. Rather than seeking to mend the relationship and garnering support from the individual, they jeopardize their physical health once more.
4.	For certain individuals, harboring grudges or regret contradicts their religious beliefs. It consistently leads to diminished peace of mind and a weakened sense of connection with others or whatever they hold sacred.
"""
)
with st.form("benefits_2.3"):
    st.text_area("""If you had to select one of the benefits listed above for your own life, which most motivates you to forgive?
""", placeholder="Type your answer here", key=2.3, max_chars=2000)
    submitted = st.form_submit_button("Submit")

st.header(
        """ :blue[Exercise 2.4]
        Reflecting on Something You’ve Forgiven in the Past
       """
)
with st.form("Reflecting_2.4"):
    st.write(
    """Forgiveness yields significant health benefits, while harboring unforgiveness has detrimental effects on well-being, as substantiated by scientific research. These exercises will guide you in integrating these findings into your life.

When you extend forgiveness to yourself or others, you endeavor to treat yourself or the individual with greater kindness, leading to a more positive outlook towards self and others. Nearly everyone has encountered numerous challenging forgiveness dilemmas. Take a moment to reflect and jot down a few sentences about the most challenging situation you've successfully forgiven. This introspection and written reflection are pivotal steps not to be overlooked.  
"""
)
    st.text_input("Please do not skip this exercise.", placeholder="Type here", key=2.4, max_chars=2000)
    submitted = st.form_submit_button("Submit")



st.header(
        """ :blue[Exercise 2.5]
              It’s Good for You to Forgive
        """
)
st.write("Are there any benefits to engaging in forgiveness?Think about the really hurtful event you forgave in Exercise 2.4, and then provide a response to the statement below regarding how much it made you feel better. ")

with st.form("good_2.5"):
    col1, col2 = st.columns(2)
    col1.write("After forgiving, I felt better physically.")
    response = col2.selectbox("Question 1", ("0 - No better (or even worse)", "1 - Somewhat better", "2 - Much better"), index=None, placeholder="Select rating")

    col1, col2 = st.columns(2)
    col1.write("After forgiving, I felt less negative and more positive psychologically or emotionally.")
    response2 = col2.selectbox("Question 2", ("0 - No better (or even worse)", "1 - Somewhat better", "2 - Much better"), index=None, placeholder="Select rating")
    
    col1, col2 = st.columns(2)
    col1.write("After forgiving, my relationship got better.")
    response3 = col2.selectbox("Question 3", ("0 - No better (or even worse)", "1 - Somewhat better", "2 - Much better"), index=None, placeholder="Select rating")

    col1, col2 = st.columns(2)
    col1.write("After forgiving, I felt spiritually more connected.")
    response3 = col2.selectbox("Question 4", ("0 - No better (or even worse)", "1 - Somewhat better", "2 - Much better"), index=None, placeholder="Select rating")

    submitted = st.form_submit_button("Submit")



st.header(
        """ :blue[Exercise 2.6]
        Experiencing Emotional Forgiveness Happens after you Decide to Forgive
       """
)
st.write(
    """Forgiveness involves making a conscious choice to pardon those who have caused us harm or pardoning oneself for something that happened in the past. Upon making this decision, we endeavor to exhibit less negativity towards those individuals or ourself, and instead aim to regard them or ourselves with appreciation. However, achieving emotional forgiveness—reducing feelings of resentment, anger, hurt, and bitterness—might require more time than simply deciding to forgive. While we may genuinely commit to forgiveness and strive to treat ourselves or the individual better, attaining complete emotional forgiveness may lag behind. Decisional and emotional forgiveness are sometimes concurrent processes, yet they remain distinct and may occur independently of each other. They can also unfold at varying paces, with either one potentially preceding the other. In fact, some individuals may experience one form of forgiveness without ever experiencing the other. Assess your comprehension by responding to the following question.
"""
)
with st.form("Decide2.6"):
    st.text_area("How are emotional and decisional forgiveness different?", placeholder="Type here", key=2.6, max_chars=2000)
    submitted = st.form_submit_button("Submit")

st.header(
        """ :blue[Exercise 2.7]
        Differences between Deciding to Forgive and Experiencing Emotional Forgiveness
       """
)
st.write(
    """Read and Think about These: 

Making a decision to forgive serves as a crucial pathway toward emotional forgiveness, repairing fractured relationships and perceptions of ones self, and attaining a deeper spiritual connection devoid of resentment. Emotional forgiveness, extensively documented in scientific literature, yields manifold benefits for physical well-being, spanning cardiovascular health, immune function, digestive health, cognitive prowess, and stress reduction. Moreover, substantial research underscores its role in mitigating depressive tendencies, anxiety disorders, anger issues, obsessive-compulsive tendencies, post-traumatic stress, and psychosomatic ailments. As previously explored, the interplay between decisions to forgive and emotional forgiveness is evident, although their impacts on health, psychology, relationships, and spirituality diverge. Both facets remain indispensable in fostering holistic well-being.

"""
)
st.header(
        """ :blue[Exercise 2.8]
        Differences between Deciding to Forgive and Experiencing Emotional Forgiveness
       """
)
st.write(
    """Throughout this session, you've gained valuable insights to aid in the process of forgiveness. 

You've come to understand that:

•	You've successfully forgiven significant transgressions in the past, demonstrating your capacity for forgiveness.

•	Forgiveness encompasses two distinct forms: the decision to forgive and the emotional aspect of forgiveness. While interconnected, they offer unique advantages.

:blue[Let's assess your comprehension through a brief recap:]

•  The primary health benefits predominantly manifest in your cardiovascular and immune systems.

•	Psychological advantages stem from reduced tendencies to fret or fixate on past grievances.

•	In terms of relationships, the decision to forgive alters your treatment of the wrongdoer, paving the way for positive changes in interpersonal dynamics.
"""
)

st.header(
        """ :blue[Lesson 3]
        The Decision to Forgive
       """
)
st.write(
    """At times, decisions to forgive are deliberate and consciously made. Conversely, there are instances where we gradually find ourselves making important decisions almost unconsciously. If someone in the military has been betrayed by a respected superior, for example, that service member often progresses towards deeper commitments through small, incremental steps. This lesson provides an opportunity for you to intentionally choose forgiveness. If you've already started down the path of forgiveness, you can reaffirm your commitment to it.

In Lesson 2, you learned about the myriad ways in which withholding forgiveness can harm your health, relationships, and inner peace. You were presented with scientific evidence supporting the act of forgiveness. Moreover, you understand that harboring resentment towards someone or yourself is not only futile but also detrimental to your well-being.

Perhaps you're reflecting on the pain you've endured and recognize that you've already begun the journey towards forgiveness. Alternatively, you may be contemplating a conscious commitment to forgiveness. Whether you're already on the path or preparing to embark upon it, this lesson aims to solidify your decision and guide you towards a firmer resolve.

"""
)

st.header(
        """ :blue[Exercise 3.1]
              Feelings of Injustice
        """
        )

st.write("Rank – based on how you think you would feel – the hypothetical statements below from easiest to forgive (rank 1) to most difficult to forgive (rank 4). ")

with st.form("feeling_3.1"):
    
    col1, col2 = st.columns(2)
    col1.write("Person A hurt you deeply and yet repeatedly says, “I didn’t do anything wrong.")
    role_res = col2.radio('Pick one:', [1, 2, 3, 4], index=None, horizontal=True, key=3.1)

    col1, col2 = st.columns(2)
    col1.write("Person B didn’t really hurt you that badly.")
    role_res = col2.radio('Pick one:', [1, 2, 3, 4], index=None, horizontal=True, key=3.2)

    col1, col2 = st.columns(2)
    col1.write("Person C hurt you deeply but cried and apologized sincerely.")
    role_res = col2.radio('Pick one:', [1, 2, 3, 4], index=None, horizontal=True, key=3.3)

    col1, col2 = st.columns(2)
    col1.write("Person D hurt you deeply but apologized and did some nice things to make up for the hurt.")
    role_res = col2.radio('Pick one:', [1, 2, 3, 4], index=None, horizontal=True, key=3.4)

    
    st.write(
    """Typically, individuals tend to categorize these wrongs in the following sequence: A = 4 (most challenging to forgive); B = 1 (least difficult); C = 3; D = 2. This ranking correlates with the level of injustice still perceived. The "injustice gap" represents the disparity between the offense committed and the efforts made to rectify or alleviate it. When a wrongdoer offers an apology and takes steps to mitigate the harm caused, they effectively diminish some of this injustice. The magnitude of the injustice gap directly influences the difficulty of attaining complete forgiveness."""
)
    submitted = st.form_submit_button("Submit")



st.header(
        """ :blue[Exercise 3.2]
              Forgiveness is a Decision
        """
)
st.write("Individuals are not obligated to forgive; there are various methods to diminish their sense of injustice. For each method listed below, consider whether you perceive it as a favorable or unfavorable approach to minimizing the injustice gap.")

with st.form("forgive_3.2"):
    col1, col2 = st.columns(2)
    col1.write("See justice done.")
    response = col2.selectbox("Question 1", ("Good", "Bad"), index=None, placeholder="Select rating", key=3.5)

    col1, col2 = st.columns(2)
    col1.write("Excuse the person’s hurtful behavior because he or she did not mean to hurt you.")
    response2 = col2.selectbox("Question 2", ("Good", "Bad"), index=None, placeholder="Select rating", key=3.6)
    
    col1, col2 = st.columns(2)
    col1.write("Let God exact justice.")
    response3 = col2.selectbox("Question 3", ("Good", "Bad"), index=None, placeholder="Select rating", key=3.7)

    col1, col2 = st.columns(2)
    col1.write("Don’t let your emotions trigger your actions.")
    response3 = col2.selectbox("Question 4", ("Good", "Bad"), index=None, placeholder="Select rating", key=3.8)

    col1, col2 = st.columns(2)
    col1.write("Justify the person’s behavior because you have hurt them too.")
    response2 = col2.selectbox("Question 2", ("Good", "Bad"), index=None, placeholder="Select rating", key=3.9)
    
    col1, col2 = st.columns(2)
    col1.write("Accept and move on with your life.")
    response3 = col2.selectbox("Question 3", ("Good", "Bad"), index=None, placeholder="Select rating", key=3.91)

    col1, col2 = st.columns(2)
    col1.write("Get even.")
    response3 = col2.selectbox("Question 4", ("Good", "Bad"), index=None, placeholder="Select rating", key=3.92)

    st.write(" :blue[Forgiveness isn't always a prerequisite for narrowing the injustice gap. However, for certain transgressions, this gap may persist despite efforts to reconcile. Nevertheless, even if the injustice gap remains, you still retain the ability to forgive.]")

    submitted = st.form_submit_button("Submit")






st.header(
        """ :blue[Exercise 3.3]
        Making a Decision to Forgive Can Release Unforgiveness
       """
)
st.write(
    """Although forgiveness is not obligatory, you can actively choose to pursue it. Visualize holding your hands together and extending your arms as far away from your body as possible, imagining the weight of hurt and unforgiveness resting in your grasp. If you're not prepared to release this burden yet, hold onto it for another 30 seconds. As your arms tire, contemplate the myriad possibilities awaiting your hands and your life if you could simply let go and move forward. Recognize that clinging to this burden only inflicts pain upon yourself, not the wrongdoer, whereas releasing it benefits both parties.

Even if you're not ready to completely relinquish this burden, gradually open your hands and allow your arms to return to their natural position. Embrace the sense of relief that follows, and embrace it fully when you're prepared to commit to forgiveness.

Now that you understand the advantages of forgiveness, are you willing to genuinely decide to forgive? This entails releasing the desire for retribution and instead choosing to regard the yourself or a wrongdoer as a valuable albeit imperfect individual. 

In Lesson 1, you assessed your decision to forgive on a scale. Full decisional forgiveness (rated 10) meant relinquishing the desire for retaliation (to self or others) and choosing to value self or others despite previous actions. Conversely, zero decisional forgiveness involved seeking revenge, severing ties, or intending to harm self or others. Your rating may have evolved since then. Take a moment to contemplate your current progress toward forgiving the hurt. Hopefully, you've moved closer to a decision to value yourself or the other person compared to Lesson 1. Assign yourself a new rating on a scale from 0 (no decisional forgiveness) to 10 (complete decision to forgive).

"""
)


with st.form("release_3.3"):
    col1, col2 = st.columns(2)
    col1.write("Assign yourself a new rating on a scale from 0 (no decisional forgiveness) to 10 (complete decision to forgive).")
    role_res = col2.radio('Pick your rating here:', [1, 2, 3, 4, 5, 6, 7, 8, 9, 10], index=None, horizontal=True, key=4.1)

    submitted = st.form_submit_button("Submit")

st.header(
        """ :blue[Exercise 3.4]
        The Requirement of Decisional Forgiveness + Emotional Forgiveness
       """
)
st.write(
    """Do you believe you've genuinely committed to forgiving this wrongdoing? Or do you sense that you've at least taken steps in that direction? You'll have another opportunity to evaluate your progress after engaging with the lessons on emotional forgiveness.

It's crucial to recognize that making a decision to forgive differs significantly from experiencing emotional forgiveness. Simply making the decision doesn't automatically lead to inner peace; it's a more complex process.

While deciding to forgive is a crucial initial step, it alone isn't sufficient to address the emotional aspect. Achieving emotional forgiveness involves actively engaging in a series of 6 steps outlined in the BREACH/PREACH forgiveness model. The subsequent sections of the workbook will guide you through these steps. Let's embark on the journey of working through these five steps to REACH Forgiveness.

"""
)

st.header(
        """ :blue[Exercise 3.5]
        Consider your Motivations
       """
)
with st.form("motivation_3.5"):
    st.write(
    """In the previous lesson, you discovered that opting to forgive primarily enhances relationships, the view of oneself, and spirituality, whereas emotional forgiveness predominantly bolsters physical and mental well-being. Considering these benefits, which aspect resonates with you the most and serves as the primary motivation for pursuing forgiveness?
"""
)
    st.text_area("Write them below:", placeholder="Type here", key=4.2, max_chars=2000)
    submitted = st.form_submit_button("Submit")


st.header(
        """ :blue[Exercise 3.6]
        Getting Practical with Forgiveness
       """
)
st.write(
    """Becoming a more forgiving individual extends beyond completing this workbook; it requires consistent practice of forgiveness in daily life. To facilitate this process, it's beneficial to establish daily reminders that prompt forgiveness rather than harboring resentment, bitterness, or anger towards those who wrong you. Consider implementing the following suggestions as reminders:
1.	Acknowledge that [____ experience] often triggers feelings of bitterness, resentment, or anger within you. Commit to calming yourself immediately upon the thought of encountering this situation or person, finding peace through forgiveness. Practice deep breathing exercises, exhaling anger and inhaling a sense of well-being. Additionally, strive to avoid dwelling on thoughts that evoke bitterness, resentment, or anger.
2.	Recognize the challenge of returning to a task after stepping away from it, even with the best intentions. To ensure completion of the workbook's lessons, schedule a specific time to resume and finish it, preemptively adding it to your calendar. Place reminders of this designated time in your living space to reinforce your commitment.
3.	When you catch yourself entertaining thoughts of anger, bitterness, or resentment, actively calm your mind. Furthermore, revisit the workbook's lessons on calming techniques.
4.	Take proactive steps to address instances of hurt or offense promptly. Schedule a specific time in your calendar to work on forgiving the individual responsible for the recent event before allowing it to escalate and affect your emotions.

"""
)
with st.form("practical_3.6"):
    st.text_area("Write the numbers for each situation you have committed to doing.", placeholder="I have committed to…", max_chars=2000, key=4.3)
    submitted = st.form_submit_button("Submit")


st.header(
        """ :blue[Exercise 3.7]
        Knowledge Assessment
       """
)
st.write("Now, you have learned various tips that will help you engage in forgiveness. Specifically, you’ve learned that:")

with st.form("my_form"):
    col1, col2 = st.columns(2)
    col1.write("You can decide to forgive. Is there any harm that is too big to forgive?")
    response = col2.selectbox("Question 1", ("yes", "No"), index=None, placeholder='select your answer ["Yes" or "No"]')

    col1, col2 = st.columns(2)
    col1.write("The decision to forgive and emotional forgiveness are vital. Is either one is easier to do than the other? ")
    response2 = col2.selectbox("Question 2", ("yes", "No"), index=None, placeholder='select your answer ["Yes" or "No"]')
    
    col1, col2 = st.columns(2)
    col1.write("Why?")
    response3 = col2.text_area("Question 3", placeholder="Write your answer below:", max_chars=2000)

    submitted = st.form_submit_button("Submit")


st.write(
    """It is the consensus of scientists and counselors that both decisional and emotional forgiveness hold significance. 
    Engaging in both processes is beneficial. Decisional forgiveness involves consciously choosing to treat yourself or a wrongdoer
    with greater positivity, recognizing the inherent value in being human. Emotional forgiveness, on the other hand, entails investing 
    the time and effort necessary to replace unforgiving emotions with positive ones, reflecting an appreciation for the value of all individuals."""
)

st.divider()
st.divider()

st.header(
        """ :blue[Lesson 4]
        BREACH/PREACH Model
B or P = Betrayal or Perpetration Moral Injury Must be Understood
R = Recall the Hurt"""
)
st.header(
    """ :blue[Exercise 4.1]
Change Your Mindset
"""
)
st.write(
    """When individuals experience profound hurt, they may perceive forgiveness as an insurmountable task. Perhaps the situation that caused the pain is one that you may not be able to revisit again (e.g., you injured innocent civilians during a deployment and you are now retired from active duty service). 

However, this doesn't mean forgiveness is unattainable, even if a wrongdoer doesn't merit it or you will not be able to redeem yourself in a certain context. Developing forgiveness is akin to strengthening a muscle; it requires exertion and perseverance. Just as exercising a weary muscle entails discomfort, committing to forgiveness may initially feel arduous. This is why practicing forgiveness in various scenarios is crucial; it cultivates resilience and fortitude, akin to building strength in a "forgiveness muscle."

Two distinct mindsets exist: fixed mindsets and growth mindsets. While fixed mindsets may seem reassuring, they often perpetuate stagnation. Conversely, growth mindsets embrace change and evolution, recognizing the potential for growth. With a growth mindset, the future remains malleable and open to transformation.

It's important to note that deciding to forgive is most closely associated with relational benefits, and for many, it holds spiritual significance as well. While decisions can yield physical and psychological advantages, they may not always be readily apparent. As you embark on the journey to practice the 6 steps of emotional forgiveness outlined in the BREACH/PREACH model, remember that emotional forgiveness is intimately linked with physical and psychological well-being. Each letter of BREACH/PREACH corresponds to a crucial aspect of the forgiveness process: Betrayal or Perpetration Moral Injury Knowledge, Recalling the Hurt, Empathizing with the Wrongdoer or the Self, Offering an Altruistic Gift of Forgiveness, Committing to the Forgiveness You've Experienced, and Holding onto Forgiveness in Times of Doubt. Over the course of the next five lessons, we will delve into each step of this process, commencing with Betrayal or Perpetration Moral Injury Knowledge and Recalling the Hurt.

"""
)

st.header(
        """ :blue[Exercise 4.2]
        Being a Forgiver is Important
       """
)
st.write(
    """The essence of forgiveness is exemplified within a family, community, or workplace when conflicts and intentional harm are set aside, 
    allowing the collective to pursue shared objectives harmoniously. Remarkably, the presence of just one forgiving individual can significantly 
    alter the dynamics of a group. Reflecting on this, consider the significance of embodying forgiveness within your familial, professional, 
    religious, communal, and national contexts. 
"""
)
with st.form("being_4.2"):
    st.text_area(
        """Share a few sentences outlining which specific group or groups you aspire to influence the most, 
    and elucidate your reasoning behind this choice.""", placeholder="Type here", key=4.21, max_chars=5000)
    submitted = st.form_submit_button("Submit")



st.header(
        """ :blue[Exercise 4.3]
        A Different Way to Describe a Hurt
       """
)
st.write(
    """In the initial section of this workbook (Exercise 1.2), you penned down the narrative of the hurt you aim to forgive and seek emotional reconciliation with. Continuously recounting the same narrative may impede our progress. Thus, we require an alternative perspective, one that is more detached and objective while remaining true to the facts. Revisit the event once more, but this time, adopt the stance of an observer rather than reliving it from your own perspective. Strive to attain greater distance from the narrative.
"""
)
with st.form("my_hurt"):
    col1, col2 = st.columns(2)
    col1.write("Write the story again, but this time without emphasizing how badly you viewed yourself or the wrongdoer or how much you have been victimized")
    response = col2.text_area("Write your answer below:", key=16, placeholder="Type your answer here", max_chars=2000)

    col1, col2 = st.columns(2)
    col1.write("What are at least three differences between the first (Exercise 1.2) and second versions of your story? (Look back if you wish.) ")
    response2 = col2.text_area("Write your answer below:", key=17, placeholder="Type your answer here", max_chars=2000)
    
    submitted = st.form_submit_button("Submit")




st.header(
        """ :blue[Exercise 4.4]
        Giving Away a Hurt: Betrayal or Perpetration
       """
)
st.write(
    """Betrayal-based moral injury within the context of military service encapsulates the profound psychological wounds inflicted upon individuals when they experience betrayal or breaches of trust within their ranks. This form of moral injury arises when soldiers, who depend on the unyielding camaraderie and loyalty of their comrades, confront instances of treachery, deceit, or abandonment. Such betrayal can manifest in various forms, including betrayal by fellow soldiers, commanding officers, or even the institution itself. Examples range from instances of betrayal during combat operations, such as desertion or abandonment on the battlefield, to betrayal within the organizational structure, such as unethical behavior or abuse of power by superiors. The ramifications of betrayal-based moral injury are profound and enduring, permeating every aspect of the individual's psychological well-being. Soldiers grappling with these wounds may experience feelings of disillusionment, anger, guilt, and profound distrust towards others, including their peers and leadership. Moreover, the erosion of trust can undermine the cohesion and morale of the entire unit, jeopardizing mission effectiveness and the overall success of military operations. 

Perpetration-based moral injury in the military context entails the profound psychological distress experienced when individuals are directly involved in or witness acts that transgress their moral code or ethical principles. This form of moral injury can arise from direct participation in actions that violate deeply held beliefs, such as causing harm to civilians or engaging in acts of brutality during combat. Additionally, witnessing the perpetration of such actions by fellow soldiers or leaders can also inflict moral injury. Soldiers may grapple with feelings of guilt, shame, and moral ambiguity as they confront the ethical ramifications of their actions or the actions of others. Moreover, the internal conflict stemming from perpetration-based moral injury can lead to profound existential questioning, erosion of self-esteem, and challenges in reintegrating into civilian life post-deployment. 
To reaffirm your readiness for the challenges ahead, let's revisit this exercise. Engaging your body in this activity, as you've done previously, will maximize its effectiveness. Stand up. Recall a previous lesson (Exercise 3.3) where you imagined holding the burden of hurt (either betrayal or perpetration) in your hands. Extend your arms outward, visualizing this hurt as something you're containing within your grasp, deliberately keeping it at a distance. After about a minute of holding this position, you'll likely feel the strain and weight, mirroring the experience of holding onto grudges.

Now, envision yourself releasing this burden. In the safety and privacy of your current surroundings, mentally affirm, "I decide to forgive myself or my wrongdoer." It's akin to transitioning from a stress-inducing website to one that brings freedom and peace with just a click. To symbolize this decision, irrespective of your readiness for emotional forgiveness at this moment, open your hands and allow your arms to fall naturally to your sides, symbolizing the release of negative emotions. You may choose to perform this exercise while holding a physical object representing the hurt.

Consider making a genuine decision to forgive if you haven't already. This decision doesn't necessarily alter your feelings significantly; however, it sets the stage for emotional forgiveness in the upcoming sections. Remember, practicing decisional forgiveness involves recalling the betrayal or perpetration-based hurt, deciding to act positively towards the individual, and relinquishing grudges. You can revisit this process later as you work on changing your feelings. If you're unable to decide to forgive at this moment, know that it may become easier with time.

"""
)
st.header(
        """ :blue[Exercise 4.5]
        Our Reasons for Doing Things
       """
)
st.write(
    """Reflect on a situation where you inadvertently caused harm to someone. Describe your thoughts, emotions, observations, and actions leading up to, during, and following the incident. Consider the motivations and intentions behind your actions, recognizing that individuals often act with what they perceive to be good reasons, even if these reasons may not resonate with those who have been hurt (e.g., some innocent civilians being killed during a mission that aims to bring down a maleficent terrorist). Acknowledge that, like everyone else, you too have unintentionally hurt others despite your best intentions. While challenging, attempt to envision that you or your wrongdoer may not have intended to cause harm.
"""
)
st.header(
        """ :blue[Exercise 4.6]
        Understand the Context and the Beginning of Empathy
       """
)
with st.form("empathy"):
    col1, col2 = st.columns(2)
    col1.write('Respond below by selecting “Yes, quite a lot,” “Yes, some,” “Yes, a little,” or “Not yet.”')
    res_empathy = col2.selectbox("", ("Yes, quite a lot", "Yes, some", "Yes, a little", "Not yet."), index=None, placeholder='select your answer')
    submitted = st.form_submit_button("Submit")



st.header(
        """ :blue[Exercise 4.7]
        Knowledge Assessment
       """
)
st.write(
    """Throughout this lesson, you've acquired insights that will aid you in the journey of forgiveness. You've discovered that:

•	There are betrayal and perpetration based moral injuries, both of which carry significant hurt.

•	You have the power to relinquish the burden of hurt. It can be as straightforward as unclenching your fists and releasing a tightly held grudge.

•	Opting to forgive can offer immediate relief, providing a sense of lightness and liberation.

•	However, despite making the decision to forgive, you may still find yourself grappling with feelings of resentment, bitterness, hostility, hatred, anger, and anxiety. While these emotions can be overcome, they often linger and resurface intermittently, proving to be unexpectedly potent.
""")
with st.form("Assessment"):
    st.text_input(
    """The process of replacing these negative emotions with positive ones is termed (E______ F______), a journey that demands time and dedicated effort.""", placeholder='E______  and F______')
    submitted = st.form_submit_button("Submit")



st.divider()

st.header(
        """ :blue[Lesson 5]
        E = Empathy for Yourself or the One Who Hurt You
       """
)
st.write(
    """During this lesson, you’ll persist in trying to understand the person who hurt you and even develop empathy  for them. Or, you may try to understand yourself better if you have experienced a perpetration based moral injury and empathize more with yourself by understanding the context. 

This exercise holds significant value in fostering forgiveness, ranking among the most crucial steps. Research indicates that engaging in this straightforward, 10-minute activity can notably enhance one's capacity to forgive others.

"""
)


st.header(
        """ :blue[Exercise 5.1]
        Role Play
       """
)
st.markdown(
    """Write a hypothetical conversation between you and a trusted counselor. What do you say? 

<span style="color:orange;font-weight:bold;">Example</span>:

<span style="font-weight:bold;">Counselor</span>: 	It seems like there's a significant burden you're carrying related to a specific incident. Can you tell me more about what happened?

<span style="font-weight:bold;">Me</span>:	Yeah, during a mission, we were targeting an enemy, but in the chaos, an innocent civilian was unintentionally killed. It's been haunting me ever since.

<span style="font-weight:bold;">Counselor</span>: 	That must have been an incredibly distressing situation to find yourself in. It sounds like you were faced with a difficult choice and the consequences are weighing heavily on you.

<span style="font-weight:bold;">Me</span>:	Exactly. I know we were trying to take down a dangerous threat, but I can't shake off the fact that an innocent person lost their life because of our actions.

<span style="font-weight:bold;">Counselor</span>: 	It's understandable to feel conflicted about this experience. It's not uncommon for service members to grapple with moral dilemmas in the midst of combat, especially when trying to navigate between protecting others and accomplishing the mission.

<span style="font-weight:bold;">Me</span>:	I keep questioning if there was something else I could have done to prevent it.

<span style="font-weight:bold;">Counselor</span>:	It's natural to reflect on what could have been done differently, but it's important to remember that you were operating under intense pressure and in a complex situation. Sometimes, despite our best efforts, tragic outcomes occur in order to accomplish a greater good.

<span style="font-weight:bold;">Me</span>:	I just can't shake off this feeling of responsibility. I don’t think I can forgive myself.

<span style="font-weight:bold;">Counselor</span>:	Forgiveness can be a complex and challenging process, especially in situations like this. It may take time and effort, but it's possible to find a sense of peace and acceptance by making a decision to forgive.
It's your opportunity now. Aim for at least three substantial interactions between yourself and the therapist. Whether this dialogue occurs in reality is irrelevant, but striving for accuracy remains beneficial. The crucial aspect is comprehending the scenario's context and maintaining objectivity regarding the events.

""", unsafe_allow_html=True
)
with st.form("role"):
    st.text_area("Type your dialogue below:", max_chars=5000)
    st.write(
    """Have you taken into account the circumstances? The stressors at play? The motivations behind your actions or the actions of the other individual? List below additional factors you may have overlooked that could aid in gaining a deeper understanding of the situation.
    """
)
    st.text_area("Type below:", key=18, max_chars=2000)


    st.write(
    """Now, and this is crucial, position an unoccupied chair opposite you and verbalize your dialogue audibly. Alternate between sitting in one chair for your lines and the other for the other person's lines. Engage in this imagined conversation between you and the counselor or you and the other person for five to ten minutes, switching chairs every few seconds. Research indicates that if you approach this exercise earnestly, it can be the most potent emotional step towards forgiving the wrongdoer or yourself.

"""
)
    st.text_area(" :blue[Do you have any new insights now that you are putting yourself in the other person’s place? What are they?]", placeholder="Type Here", key=20, max_chars=2000
)
    st.text_area(" :blue[What have you realized about the person’s motives and feelings (or your own motives)? Do you better understand their (or your) feelings and reasoning?]", placeholder="Type Here", key=21, max_chars=2000
)

    st.write(" :blue[Answer the following five questions:]")

    col1, col2 = st.columns(2)
    col1.write("Are there any reasons to feel sorry for yourself or the person who offended you?")
    role_res = col2.text_area("", placeholder="Type Here", key=26, max_chars=2000)

    col1, col2 = st.columns(2)
    col1.write("Does he or she need forgiveness? Do you need forgiveness?")
    role_res = col2.text_area("", placeholder="Type Here", key=22, max_chars=2000)

    col1, col2 = st.columns(2)
    col1.write("From himself or herself? For you?")
    role_res = col2.text_area("", placeholder="Type Here", key=23, max_chars=2000)

    col1, col2 = st.columns(2)
    col1.write("From you? ")
    role_res = col2.text_area("", placeholder="Type Here", key=24, max_chars=2000)

    col1, col2 = st.columns(2)
    col1.write("Do you feel any sorrow on behalf of the person or yourself?")
    role_res = col2.text_area("", placeholder="Type Here", key=25, max_chars=2000)

    st.write("Experiencing empathy, sympathy, compassion, or affection towards yourself or the individual who caused you harm diminishes your feelings of resentment and unwillingness to forgive.")

    submitted = st.form_submit_button("submit")



st.header(
        """ :blue[Exercise 5.2]
        Compassion
       """
)
st.write(
    """Perhaps you find it challenging to empathize. You might genuinely believe that you or the individual who harmed you is inherently malicious, foolish, and unkind. Rather than attempting to empathize, can you acknowledge that you or this person requires your compassion, despite their actions?

Compassion involves recognizing that someone may be in need of assistance, even if they aren't actively seeking it or willing to accept it. However, you can perform a selfless deed by envisioning a compassionate response, even if you or the individual doesn't seem deserving of it.

"""
)
with st.form("compassion"):
    col1, col2 = st.columns(2)
    col1.write("How much compassion do you feel for yourself or the person who hurt you? [Designate your present feelings by selecting the correct one]")
    role_res = col2.selectbox("", ('None', 'A little', 'A moderate amount', 'A lot'), index=None, placeholder='select your answer', key=27.0)


    col1, col2 = st.columns(2)
    col1.write("What could you do to feel more compassion toward yourself or that person? ")
    compassions = col2.text_area("", placeholder="Type your answer below", key=27, max_chars=2000)

    submitted = st.form_submit_button("submit")


st.header(
        """ :blue[Exercise 5.3]
        Practical Tips for Daily Life
       """
)

with st.form("daily_life"):
    st.text_area(
    """List the next two or three times that you expect to see the person who harmed or offended you. Alternatively, 
    list the next 3 circumstances in which you might be reminded of a perpetration-based event that you committed. """, max_chars=2000)
    st.write("Imagine yourself in each instance. Imagine feeling more empathic each time. Can you use that mental picture to think more empathically about yourself or the other person? ")
    submitted = st.form_submit_button("submit")


st.header(
        """ :blue[Exercise 5.4]
        Other Types of Emotions Relevant to the Situation
       """
)
with st.form("emotions"):
    st.text_area(
    """Consider two other emotions (except for empathy and compassion) that might serve as a substitute for some of your negative emotions? List them. """, max_chars=2000)
    submitted = st.form_submit_button("submit")


st.header(
        """ :blue[Exercise 5.5]
        How Much Forgiveness
       """
)
st.write('How much of the negative emotion do you think you do need to replace with positive emotion to achieve "full forgiveness"?')
with st.form("forgiveness"):
    col1, col2 = st.columns(2)
    col1.write("For a stranger who hurt you (for example, a thief who stole your money and identity papers) or a stranger that you harmed, would you need to [Indicate one of the following by bold font]")
    role_res = col2.selectbox("", ('Eliminate most of the negative emotion', 'Eliminate all of the negative emotion', 'Eliminate all of the negative emotion and feel positive emotion'), index=None, placeholder='select your answer', key=28)

    col1, col2 = st.columns(2)
    col1.write("For a person who hurt you or you hurt and whom you are no longer able to be around, would you need to [Indicate one by bold font]")
    role_res = col2.selectbox("", ('Eliminate most of the negative emotion', 'Eliminate all of the negative emotion', 'Eliminate all of the negative emotion and feel positive emotion'), index=None, placeholder='select your answer', key=29)

    col1, col2 = st.columns(2)
    col1.write("For a loved one you see every day who hurt you or that you hurt, would you need to [Indicate one by bold font]")
    role_res = col2.selectbox("", ('Eliminate most of the negative emotion', 'Eliminate all of the negative emotion', 'Eliminate all of the negative emotion and feel positive emotion'), index=None, placeholder='select your answer', key=30)

    submitted = st.form_submit_button("submit")

st.header(
        """ :blue[Exercise 5.6]
        Knowledge Assessment
       """
)
with st.form("Assessments"):
    st.text_input(
        """Throughout this session, you've delved deeper into the dynamics of forgiveness, uncovering valuable insights that can profoundly impact your journey towards healing. Central to this understanding is the recognition that negative emotions such as resentment, bitterness, anger, and hate can be effectively countered by two powerful emotions: E__________ and C___________.

Empathy, the ability to understand and share the feelings of another, allows you to step into the shoes of the wrongdoer, gaining insight into their motivations and experiences. By empathizing with their perspective, you can begin to see the situation from a broader and more empathetic lens, fostering a sense of connection and understanding.

On the other hand, Compassion plays a crucial role in transforming your response to the wrongdoing. It involves extending kindness and understanding towards both yourself and the wrongdoer, acknowledging the complexities of human nature and the capacity for growth and change. Through compassion, you can release the grip of negative emotions and cultivate a sense of peace and acceptance.

By integrating empathy and compassion into your forgiveness journey, you can not only alleviate the burden of resentment and anger but also pave the way for genuine healing and reconciliation.
""", placeholder="complete here: E__________ and C___________.", key=32)
    submitted = st.form_submit_button("submit")

st.divider()

st.header(
        """ :blue[Lesson 6]
        A = Give an Altruistic Gift of Forgiveness
       """
)

st.header(
        """ :blue[Exercise 6.1]
        Forgiveness is Useful
       """
)
with st.form("Useful_6.1"):
    st.text_area("If you were an extremely forgiving individual, how would that help you?", placeholder="Write at least one way below:", key=33, max_chars=2000)
    st.write("Studies indicate that individuals who forgive for their own well-being experience improvements in health, attitude, reconciliation with a wrongdoer, and spiritual contentment.")
    submitted = st.form_submit_button("submit")

st.header(
        """ :blue[Exercise 6.2]
        Have you done something Altruistic (Unselfish) for someone else?
       """
)
st.write("Reflect on a moment when you engaged in an altruistic or selfless act to aid another individual. Detail the specific action you took and articulate your emotions and thoughts surrounding the experience.")
with st.form("Unselfish"):
    col1, col2 = st.columns(2)
    col1.write("Type what you did:")
    role_res = col2.text_area("", placeholder="Type your answer below", key=34, max_chars=2000)

    col1, col2 = st.columns(2)
    col1.write("Type what you felt:")
    role_res = col2.text_area("", placeholder="Type your answer below", key=35, max_chars=2000)

    submitted = st.form_submit_button("submit")

st.header(
        """ :blue[Exercise 6.3]
        Everyone Messes Up
       """
)
st.write(
    """Yehiel Dinur, a Holocaust survivor, testified during the trial of the notorious Nazi war criminal Adolf Eichmann. Upon entering the courtroom and facing Eichmann, the man responsible for orchestrating the deaths of millions, Dinur was overcome with emotion. However, his tears and collapse were not fueled by anger or resentment. In a later interview, Dinur revealed that what struck him most was a haunting realization about himself. He confessed, "I was afraid of myself... I saw that I am capable of doing this... Exactly like he." In a moment of profound clarity, Dinur recognized the potential for evil within all individuals, including himself. He concluded that the essence of Eichmann resides within every human being.

Additionally, a musician named Sufjan Stevens once wrote a song about famous serial killer John Wayne Gacy. John Wayne Gacy, who many consider to be one of the most maleficent persons to ever live, was an American serial killer who was convicted of sexually assaulting and murdering at least 33 teenage boys and young men between 1972 and 1978. He lured many of his victims to his home in Illinois under the guise of offering them work or money, then proceeded to assault and murder them. Gacy often buried his victims in the crawl space beneath his house or disposed of their bodies in nearby rivers. He was arrested in 1978 after one of his victims managed to escape and alert the police. Gacy was ultimately convicted of multiple counts of murder and sentenced to death. The final lyric in Sufjan Stevens song goes like this: “And in my best behavior, I am really just like him. Look beneath the floor boards for the secrets I have hid.” 

"""
)
st.write(" :blue[Answer these two questions:]")
with st.form("Messes"):
    col1, col2 = st.columns(2)
    col1.write("What is the point of these stories? Do you agree with it? Why or why not?")
    role_res = col2.text_area("", placeholder="Type your answer below", key=36, max_chars=2000)

    col1, col2 = st.columns(2)
    col1.write("Did Yehiel Dinur think that he was similar to Adolf Eichmann before his realization? Type yes or no below:")
    role_res = col2.text_area("", placeholder="Type your answer below", key=37, max_chars=2000)

    submitted = st.form_submit_button("submit")

st.header(
        """ :blue[Exercise 6.4]
        When Did You Need Forgiveness?
       """
)
st.write("Reflect on a moment in your past when you caused harm or made a mistake, seeking forgiveness and receiving it. This could be a memory from your childhood, school years, work, military deployment, university, or within your family or relationships. The key is that you recognize your wrongdoing, felt remorse, and were ultimately forgiven.")
with st.form("need_forgiveness"):
    col1, col2 = st.columns(2)
    col1.write("Write a description of the event:")
    role_res = col2.text_area("", placeholder="Type your answer here", key=38, max_chars=2000)

    st.write(" :blue[Now, write a few words in response to the following questions.]")

    col1, col2 = st.columns(2)
    col1.write("1. What did it feel like to be in trouble, to lose respect from others or yourself, and to need forgiveness? (Did you feel this, even though no one was “making” you feel guilty?)")
    role_res = col2.text_area("", placeholder="Type your answer here", key=39, max_chars=2000)

    col1, col2 = st.columns(2)
    col1.write("2. What did it feel like (or would have felt like) when you asked for forgiveness from the person you hurt and you received it? Were you humbled?")
    role_res = col2.text_area("", placeholder="Type your answer here", key=40, max_chars=2000)

    submitted = st.form_submit_button("submit")

st.header(
        """ :blue[Exercise 6.5]
        Understanding the Gratitude We Feel for Forgiveness 
       """
)
st.write("Take a moment to reflect on the profound sense of relief and liberation you experienced when you received forgiveness, and how it lifted the weight of guilt from your shoulders. As you remember this feeling of gratitude or appreciation, proceed with the next exercise.")
with st.form("gratitude"):
    col1, col2 = st.columns(2)
    col1.write(" :blue[Exercise:] If you had to write a letter of gratitude after being forgiven, what would you write?")
    role_res = col2.text_area("", placeholder="Write a few notes here", key=43, max_chars=2000)

    submitted = st.form_submit_button("submit")


st.header(
        """ :blue[Exercise 6.6]
        Forgiving is a Gift  
       """
)
st.write("Imagine the person who hurt you in the scenario you have chosen for this workbook. If your scenario involves yourself and something that you have done, consider the context again. If the other person were in trouble, would you help? Write about the things you would be willing to do for that person. If the scenario involves yourself, consider the context and think about what it would be like to experience the gift of forgiveness.")
with st.form("gift"):
    col1, col2 = st.columns(2)
    col1.write("What would it feel like to receive forgiveness?")
    role_res = col2.text_area("", placeholder="Type your answer below", key=44, max_chars=2000)

    submitted = st.form_submit_button("submit")



st.header(
        """ :blue[Exercise 6.7]
        An Important Question
       """
)
st.write(
    """Consider the emotions you experienced when you received forgiveness and reflect on the satisfaction derived from performing an altruistic deed, even when the recipient may not deserve it. Wouldn't you desire to extend emotional forgiveness to the individual who caused you pain or to yourself for a certain circumstance?

About what percent of the negative emotions have you replaced since Exercise 1.4? 
""")
st.write(" :blue[Fill in the blank box below] ")

with st.form("Question"):
    col1, col2 = st.columns(2)
    col1.write("I have forgiven myself or the person who hurt or offended me")
    role_res = col2.slider("I have forgiven myself or the person who hurt or offended me", min_value=0, max_value=100, key=45)


    st.write(
        """At the beginning of this workbook, you assessed your emotional forgiveness. Now, having contemplated emotional forgiveness, its advantages, and engaging in selfless acts towards those who may not deserve it, please reevaluate your emotional forgiveness at this stage.

Emotional forgiveness entails the extent to which you genuinely sense that your emotions towards yourself or the individual who wronged or hurt you have transitioned from predominantly negative to more positive. 
""")
    col1, col2 = st.columns(2)
    col1.write("On a scale of 0 to 10, where 0 signifies no forgiveness experienced and 10 denotes complete forgiveness experienced, describe the level of emotional forgiveness you have undergone since your initial assessment.")
    role_res = col2.radio('Pick one:', [1, 2, 3, 4, 5, 6, 7, 8, 9, 10], horizontal=True, key=46)


    st.write("Keep in mind that emotional forgiveness correlates with enhanced physical and mental well-being. This positive health outcome can manifest either prior to or following the choice to forgive. If you find yourself experiencing emotional forgiveness without having made a deliberate decision to forgive, would you like to make that decision now? Opting for decisional forgiveness is associated with improved relationships and spiritual fulfillment, setting you on a path toward enhanced physical and mental health.")

    submitted = st.form_submit_button("submit")

st.header(
        """ :blue[Exercise 6.8]
        Knowledge Assessment
       """
)
with st.form("Assessments_6.8"):
    st.text_input(
        """During this lesson, you learned a lot that will facilitate forgiveness. You’ve learned that 
•	When you extend emotional forgiveness, you're offering an act of altruism—a gift bestowed regardless of deserving it.
•	At some point, you likely received the altruistic gift of forgiveness from someone you wronged, granting you a sense of freedom and lightness.
•	You experienced G____________.
•	Even if the person who wronged you is unaware, may never learn of your gesture, or might not reciprocate the gratitude you once felt, performing a kind, noble act remains significant. Your actions reflect your character, not their response.
•	Through this workbook, you may have chosen to bestow the gift of forgiveness upon yourself or the wrongdoer.  It is a transformative gift.

""", placeholder="complete here: G__________ .", key=47)
    submitted = st.form_submit_button("submit")

st.divider()
st.header(
    """ :blue[Lesson 7]
    C = Commit to the Forgiveness You Experienced
    """)

st.header(
        """ :blue[Exercise 7.1]
        Commit to Forgiveness By Writing  
       """
)
st.write("Imagine the person who hurt you in the scenario you have chosen for this workbook. If your scenario involves yourself and something that you have done, consider the context again. If the other person were in trouble, would you help? Write about the things you would be willing to do for that person. If the scenario involves yourself, consider the context and think about what it would be like to experience the gift of forgiveness.")
with st.form("commit"):
    col1, col2 = st.columns(2)
    col1.write("Write about how much you have emotionally forgiven yourself or others (so far) and how that feels.")
    role_res = col2.text_area("", placeholder="Type your answer here", key=48, max_chars=2000)

    submitted = st.form_submit_button("submit")



st.header(
        """ :blue[Exercise 7.2]
        Your Certificate of Emotional Forgiveness  
       """
)
st.write(" :blue[Complete the following:]")
with st.form("certificate"):
    date = st.date_input("Date:")
    forgiven_person = st.text_input("Forgiven Person:")
    reason = st.text_area("Reason for Forgiveness:")
    forgiveness_percent = st.slider("Percentage of Forgiveness:", 0, 100, 0)
    signature = st.text_input("Your Signature:")


    st.markdown(f"I AFFIRM TO MYSELF THAT AS OF THE DATE OF **{date}**, I HAVE DECIDED TO FORGIVE **{forgiven_person}** FOR **{reason}**. TO DATE, I HAVE FORGIVEN **{forgiveness_percent}%** OF THE EMOTIONAL UNFORGIVENESS.")
    st.markdown(f"SIGNED **{signature}**")

    submitted = st.form_submit_button("submit")

st.header(
        """ :blue[Exercise 7.3]
        What if my forgiveness is not complete?  
       """
)
st.write(
    """If you haven't achieved complete emotional forgiveness, consider revisiting the steps.  You may want to revisit Lessons 5 and 6, focusing on empathizing with yourself or the wrongdoer and cultivating a selfless or merciful form of love. These emotions can effectively replace feelings of unforgiveness, much like empathy and compassion.  In cases where you and the wrongdoer have a history of mutual hurt, whether through significant incidents or numerous small ones, you don't need to recall every instance of harm to forgive effectively. You can forgive by following three steps:

•	Select two or three of the most significant acts of hurt, which will symbolize all the harm inflicted.

•	Address each of these acts individually until forgiveness is achieved.

•	Eventually, you'll reach a point where you've forgiven enough acts, leading to complete forgiveness of self or others.
"""
)

st.header(
        """ :blue[Exercise 7.4]
        Washing Your Hands 
       """
)
st.write(
    """
    •	With an ink pen, write a short explanation of the hurt, or even just the word “HURT,” on your hand.

    •	Next, go to a bathroom and wash it off with soap and warm water.

    •	Were you able to remove all of the ink?

Lesson: We can go through the BREACH/PREACH forgiveness steps once, which may not completely eliminate our negative emotions, but it can alleviate them. With each repetition, the weight of these unforgiving feelings gradually lessens until we are liberated from them entirely.

"""
)


st.header(
        """ :blue[Exercise 7.5]
        Review of Major Concepts 
       """
)
st.write(" :blue[Quiz your memory: What are the 6 steps to BREACH/PREACH forgiveness? ]")
with st.form("mnajor"):
    col1, col2 = st.columns(2)
    col1.write("B or P =")
    role_res = col2.text_input("", placeholder="Type Here", key=49, max_chars=2000)

    col1, col2 = st.columns(2)
    col1.write("R = ")
    role_res = col2.text_input("", placeholder="Type Here", key=50, max_chars=2000)

    col1, col2 = st.columns(2)
    col1.write("E = ")
    role_res = col2.text_input("", placeholder="Type Here", key=51, max_chars=2000)

    col1, col2 = st.columns(2)
    col1.write("A =")
    role_res = col2.text_input("", placeholder="Type Here", key=52, max_chars=2000)

    col1, col2 = st.columns(2)
    col1.write("C =")
    role_res = col2.text_input("", placeholder="Type Here", key=53, max_chars=2000)

    col1, col2 = st.columns(2)
    col1.write("H = ")
    role_res = col2.text_input("", placeholder="Type Here", key=54, max_chars=2000)

    st.write(" :blue[What are our working definitions of:]")
    col1, col2 = st.columns(2)
    col1.write("Decisional forgiveness")
    role_res = col2.text_input("", placeholder="Type definition Here", key=55, max_chars=2000)

    col1, col2 = st.columns(2)
    col1.write("Experiencing emotional forgiveness")
    role_res = col2.text_input("", placeholder="Type definition  Here", key=56, max_chars=2000)
    st.write("If you do not remember, go back and check Exercises 1.3 and 1.4.")


    submitted = st.form_submit_button("submit")



st.header(
        """ :blue[Exercise 7.6]
        Controlling Your Emotions
       """
)
st.write(
    """You have the power to decide how you feel. You can choose to cling to unforgiving emotions, or if you've replaced them with feelings of love, empathy, sympathy, or compassion, you can now embrace emotional forgiveness. Even when faced with challenging circumstances that may tempt you to abandon emotional forgiveness, you still have the option to hold onto it. Psychologist Fred Luskin compares experiencing negative emotions to watching a television channel that leaves you feeling depressed, angry, fearful, or resentful. However, the key is that you can change the emotional channel. Opt for a more positive one.
"""
)
with st.form("controlling"):
    col1, col2 = st.columns(2)
    col1.write("What negative emotional channels do you often watch?")
    role_res = col2.text_input("", placeholder="Type Here", key=57, max_chars=2000)

    col1, col2 = st.columns(2)
    col1.write("What positive emotional channels do you want to watch more of?")
    role_res = col2.text_input("", placeholder="Type Here", key=58, max_chars=2000)

    col1, col2 = st.columns(2)
    col1.write("Is there something stopping you from changing emotion channels? What is it?")
    role_res = col2.text_input("", placeholder="Type Here", key=59, max_chars=2000)

    col1, col2 = st.columns(2)
    col1.write("Can you commit to change channels and seek more positive experiences?")
    role_res = col2.text_input("", placeholder="Type Here", key=60, max_chars=2000)

    col1, col2 = st.columns(2)
    col1.write("Imagine yourself switching off negative, unforgiving emotions.")
    role_res = col2.text_input("", placeholder="Type Here", key=61, max_chars=2000)

    submitted = st.form_submit_button("submit")

st.header(
        """ :blue[Exercise 7.7]
        Knowledge Assessment
       """
)
st.write(
    """In this session, you've acquired valuable insights to aid in the forgiveness process. You've discovered that:

•	Journaling about your experiences can lead to improvement.

•	Completing a forgiveness certificate, detailing the level of forgiveness you've attained, can reinforce your progress and serve as a reminder during moments of doubt, which are inevitable in matters of emotions.

If your emotional forgiveness remains incomplete, you have options:

o	Revisit Lessons #__ and #__. (If you've forgotten, consult Exercise 7.3.)

o	Utilize two alternative emotions to replace unforgiving feelings: Sympathy and Letting go.

•	You've also learned that forgiving every minor offense is not necessary to forgive the individual. Addressing two or three significant transgressions is typically sufficient to foster a sense of forgiveness.

"""
)

st.divider()
st.header(
        """ :blue[Lesson 8]
        H = Hold on to Forgiveness When You Doubt 
       """
)

st.header(
        """ :blue[Exercise 8.1]
        Might You Doubt Whether You Actually Emotionally Forgave  
       """
)
st.write("You've put in a lot of effort and have reached a point where you've either fully or partially forgiven emotionally. However, you might find yourself questioning whether your forgiveness is genuine.")
with st.form("Doubt"):
    col1, col2 = st.columns(2)
    col1.write("B or P =")
    role_res = col2._selectbox("", ("Yes", "No"), placeholder="select 'Yes' or 'No'", key=None, index=None)

    st.write(
        """Reminders of past hurts can come in two forms: "hot" reminders, such as unexpectedly encountering the person who caused the pain, facing a similar hurt from someone else, or being in a context where the original hurt occurred; and "cold" reminders, which include times when we find ourselves dwelling on past concerns."""
    )
    submitted = st.form_submit_button("submit")


st.header(
        """ :blue[Exercise 8.2]
        Hold on to Forgiveness Even When you are Experiencing a “Reminder” Situation  
       """
)
st.write(" Here are some suggestions for preventing yourself from feeling bitter or resentful when confronted with a harsh reminder.")
with st.form("Reminder"):
    col1, col2 = st.columns(2)
    col1.write("What strategies can you employ to steer your thoughts towards a more positive direction?")
    role_res = col2.text_input("", placeholder="Type Here", key=62, max_chars=2000)

    st.write("What are some situations when you might expect to experience a hot reminder in the future? How will you deal with each one?")
    col1, col2 = st.columns(2)
    col1.write("Write about three situations and how you will deal with them ")
    role_res = col2.text_input("", placeholder="Type Here", key=63, max_chars=2000)

    submitted = st.form_submit_button("submit")


st.header(
        """ :blue[Exercise 8.3]
        An Example
       """
)
st.write(
    """Recalling past injuries serves as a safeguard against repeating risky behavior. For instance, if I accidentally burn my hand on a stove, I naturally feel apprehension when my hand approaches the stove again. This response isn't about holding a grudge against the stove; rather, it's my body's instinct to shield me, warning, "You were hurt here before. Proceed with caution to avoid harm." Continuously touching a hot stove will only result in further burns. To prevent recurrence, one must alter their actions and mindset regarding the injury. Therefore, it's crucial to understand: the pain, resentment, and anxiety triggered by memories or encounters with those who caused harm do not equate to unforgiveness. When faced with the situation or individual who hurt you and experience negative emotions anew, remind yourself: the discomfort I'm feeling isn't unforgiveness, it's simply my body's defense mechanism, urging me to avoid past mistakes.
"""
)


st.header(
        """ :blue[Exercise 8.4]
        Controlling Worries  
       """
)
st.write(" Here are some suggestions for preventing yourself from feeling bitter or resentful when confronted with a harsh reminder.")
with st.form("worries"):
    col1, col2 = st.columns(2)
    col1.write("Try controlling your thoughts. Have you heard of the “white bear phenomenon”?")
    role_res = col2.write("Spend twenty seconds trying NOT to think about white bears")

    st.write("What are some situations when you might expect to experience a hot reminder in the future? How will you deal with each one?")
    col1, col2 = st.columns(2)
    col1.write("What worked and what didn’t?")
    role_res = col2.text_area("", placeholder="Type Here", key=64, max_chars=2000)

    col1, col2 = st.columns(2)
    col1.write(
        """Typically, individuals discover that giving themselves a direct order like "Don't think about white bears" actually leads them to think about white bears more often. How can you use this insight when you find yourself dwelling on the moment when someone caused you pain?""")
    role_res = col2.text_area("", placeholder="Type Here", key=65, max_chars=2000)

    submitted = st.form_submit_button("submit")

st.header(
        """ :blue[Exercise 8.5]
        Review of Ways to Hold on to Forgiveness  
       """
)
st.write(
    """ :blue[Here Are 2 Ways to Hold on to Forgiveness During a Reminder Experience]
1.	Find a way to get out of the situation.
2.	Distract yourself.

:blue[Here are 6 Ways to Hold on to Forgiveness if You Start to Worry About It]
1.	Realize that the pain of a remembered hurt is not unforgiveness.
2.	Don’t dwell on negative emotions.
3.	Remind yourself that you have forgiven yourself or the other person.
4.	Seek reassurance from a partner or friend.
5.	Use the documents that you created.
6.	Look at the 6-step model to BREACH/PREACH forgiveness, and think through the steps again.

In the future, which of these approaches do you plan to experiment with more frequently? Highlight your preferred methods using bold font or circle them with a pen to signify the ones that resonate most with you and seem most likely to be effective.

"""
)


st.header(
        """ :blue[Exercise 8.6]
        How do you know you got it?  
       """
)
st.write(
    """Psychologists emphasize the importance of repetitive practice to reinforce learning. This entails not just mindless repetition but engaging with the concepts you're trying to internalize. If you want to truly grasp emotional forgiveness, consider these straightforward yet effective steps:
1.	Share with someone significant in your life (such as a spouse, close friend, or family member) the distinction between decisional and emotional forgiveness. Additionally, articulate and explain each of the 6 steps involved in BREACH/PREACH forgiveness.
2.	Extend your understanding by teaching what you shared with the important person to five others. Research suggests that teaching is one of the most effective methods for deepening comprehension. Can you commit to teaching five individuals the disparity between decisional and emotional forgiveness, along with the 6 steps of BREACH/PREACH forgiveness?

"""
)

st.header(
        """ :blue[Exercise 8.7]
        Knowledge Assessment  
       """
)
st.write(
    """Throughout this lesson, you've gained valuable insights to help you maintain the forgiveness you've cultivated. It's natural to question the authenticity of your forgiveness and to experience anger when confronted with a situation in which you originally experienced pain. However, it's important to recognize that feeling angry doesn't invalidate your forgiveness; rather, it serves as a protective signal from your body, reminding you to proceed with caution.
If you find yourself feeling mostly forgiven yet still experience anger upon encountering a similar situation, you might reassure yourself with a thought like: "Although I feel anger in this moment, it doesn't diminish the forgiveness I've extended. My anger is a response to the past hurt, not a reflection of my current state of forgiveness."

"""
)
with st.form("knowledge_ass"):
    st.text_area("", placeholder="Type sentences here", key=67, max_chars=2000)
    submitted = st.form_submit_button("submit")

st.header(
        """ :blue[Lesson 9]
        Dedicate Yourself to Being a More Forgiving Person: 
12 Steps in 15 to 20 minutes, Part 1
 
       """
)

st.header(
        """ :blue[Exercise 9.1]
        Step 1: Why should I forgive?
 
       """
)

with st.form("Dedicate"):
    col1, col2 = st.columns(2)
    col1.write("Why do you want to be a more forgiving person? ")
    role_res = col2.text_area("", placeholder="List as many reasons as you can here", key=9.11, max_chars=2000)
    
    submitted = st.form_submit_button("submit")

st.header(
        """ :blue[Exercise 9.2]
        Step 2: Find 5 Hurts That Have Not Been Forgiven
 
       """
)
st.write(
    """List the top five significant wounds that continue to evoke negative emotions towards yourself or another individual. Provide a brief description of each of these wounds. For instance, "My immediate superior in the military sexually harassed me." Reflect on instances where (a) your fellow solider let you down, (b) you saw people do things that go against your value system, (c) your friend betrayed your trust, (d) your fellow soldiers fell short of expectations, or (e) someone caused physical harm to you or a loved one.
"""
)
with st.form("hurts"):
    col1, col2 = st.columns(2)
    col1.write("Describe your wounds:")
    role_res = col2.text_area("", placeholder="List the top five significant ones", key=9.21, max_chars=2000)
    
    st.write("By deciding to forgive and applying BREACH/PREACH forgiveness to each wound, you may become a more forgiving person.")

    submitted = st.form_submit_button("submit")

st.header(
        """ :blue[Exercise 9.3]
        Step 3: Forgive One Wound at a Time
 
       """
)
st.write(
    """As you forgive individual wounds gradually, you enhance your overall capacity for forgiveness. Select one of the injuries you outlined in Step 2. Craft a concise description for employing the BREACH/PREACH method to forgive each one.
"""
)
with st.form("wound"):
    col1, col2 = st.columns(2)
    col1.write("B or P = Is the hurt one of betrayal or perpetration?")
    role_res = col2.text_area("", placeholder="Type here", key=70, max_chars=2000)

    col1, col2 = st.columns(2)
    col1.write("R = Recall the hurt. Write a summary.")
    role_res = col2.text_area("", placeholder="Type here", key=71, max_chars=2000)

    col1, col2 = st.columns(2)
    col1.write("E = Empathize. From a sympathetic point of view, describe why you or the other person did what they did.")
    role_res = col2.text_area("", placeholder="Type here", key=72, max_chars=2000)

    col1, col2 = st.columns(2)
    col1.write("A = Altruistic gift. Thinking empathically about yourself or the wrongdoer, can you explain why you might want to unselfishly let go of negative emotions? ")
    role_res = col2.text_area("", placeholder="Type here", key=73, max_chars=2000)

    col1, col2 = st.columns(2)
    col1.write("C = Commit to any forgiveness you experienced. Write a sentence about your success in trying to forgive. If you made a decision to forgive and treat yourself or the other person better, write when you plan to do it.")
    role_res = col2.text_area("", placeholder="Type here", key=74, max_chars=2000)

    col1, col2 = st.columns(2)
    col1.write("H = Hold on to forgiveness. Write how perceive you think it would be like to make this a lasting forgiveness.")
    role_res = col2.text_area("", placeholder="Type here", key=75, max_chars=2000)
    
    st.write("Can you now make a decision to forgive yourself or that person and treat yourself or the person as a valued?")
    
    submitted = st.form_submit_button("submit")


st.header(
        """ :blue[Exercise 9.4]
        Step 4: Forgiveness Heroes
 
       """
)
st.write(
    """Identify a few people you think of as forgiveness heroes. These are people who have forgiven much and whom you admire. A forgiveness hero can be someone you know or have read/heard about.
"""
)
with st.form("heroes_9"):
    col1, col2 = st.columns(2)
    col1.write("Describe someone who you consider to be very forgiving. What makes them forgiving? How do you feel about this person?")
    role_res = col2.text_area("", placeholder="Type here", key=76, max_chars=2000)

    col1, col2 = st.columns(2)
    col1.write("Describe a historical person who you consider to be very forgiving. What makes that person forgiving?")
    role_res = col2.text_area("", placeholder="Type here", key=77, max_chars=2000)

    col1, col2 = st.columns(2)
    col1.write("Describe someone from the present whom you don’t know personally that might be a forgiveness hero.")
    role_res = col2.text_area("", placeholder="Type here", key=78, max_chars=2000)

    submitted = st.form_submit_button("submit")

st.header(
        """ :blue[Exercise 9.5]
        Step 5: Consider Yourself
 
       """
)
st.write(
    """Consider sending yourself an e-mail or text message that expresses your true desire to be a more forgiving person.
"""
)

st.header(
        """ :blue[Exercise 9.6]
        Knowledge Assessment
 
       """
)
st.write(
    """At this point in the 20-minute writing exercise aimed at fostering forgiveness, refrain from testing yourself. Instead, reserve the quiz for the conclusion of the next lesson, once all 12 steps have been covered.
"""
)


st.divider()

st.header(
        """ :blue[Lesson 10]
        Dedicate Yourself to Being a More Forgiving Person: 
12 Steps in 15 to 20 minutes, Part 2
"""
)


st.header(
        """ :blue[Exercise 10.1]
        Step 6: Make an Effort to Become More Forgiving
"""
)
with st.form("Effort"):
    col1, col2 = st.columns(2)
    col1.write("List methods you aspire to employ in cultivating a forgiving and compassionate demeanor. Pinpoint specific actions you can implement to nurture this character trait.")
    role_res = col2.text_area("", placeholder="Type here", key=79, max_chars=2000)

    submitted = st.form_submit_button("submit")

st.header(
        """ :blue[Exercise 10.2]
        Step 7: Change Your Experience with the Past
"""
)
with st.form("Past_10"):
    col1, col2 = st.columns(2)
    col1.write("While you cannot alter the past, you have the power to reshape the narrative surrounding it. Choose one of the five events you identified in Step 2, and reflect on how you intend to approach discussions about this event differently moving forward")
    role_res = col2.text_area("", placeholder="Type here", key=80, max_chars=2000)

    submitted = st.form_submit_button("submit")


st.header(
        """ :blue[Exercise 10.3]
        Step 8: Make a Strategy for Becoming More Forgiving
"""
)
with st.form("Strategy"):
    col1, col2 = st.columns(2)
    col1.write("Think of the person who hurt you or the situation in which you were hurt. Write about how you will forgive the wrongdoer or yourself from now on.")
    role_res = col2.text_area("", placeholder="Type here", key=81, max_chars=2000)

    col1, col2 = st.columns(2)
    col1.write("Will you devote yourself to giving forgiveness to offenders and yourself in the future? If so, write a simple sentence stating that intention.")
    role_res = col2.text_area("", placeholder="Type here", key=82, max_chars=2000)

    col1, col2 = st.columns(2)
    col1.write("Write about something else that you aim to do to become a more forgiving person.")
    role_res = col2.text_area("", placeholder="Type here", key=82.1, max_chars=2000)

    submitted = st.form_submit_button("submit")

st.header(
        """ :blue[Exercise 10.4]
        Step 9: Practice Forgiving Under Hypothetical Conditions
"""
)

with st.form("Hypothetical"):
    col1, col2 = st.columns(2)
    col1.write("Select one of the individuals who or situations that caused you harm from the list of five events in Step 2. Envision yourself in a room with that person or in a similar context. What unfolds in this scenario?")
    role_res = col2.text_area("", placeholder="Type here", key=83, max_chars=2000)

    submitted = st.form_submit_button("submit")

st.header(
        """ :blue[Exercise 10.5]
        Step 10: Practicing Forgiveness Everyday
"""
)
with st.form("Everyday_10"):
    col1, col2 = st.columns(2)
    col1.write(
        """Select 1 person one person or situation (Step 2) that you have the most negative emotion about. List some positive emotions that you might be able to add to that context (e.g., although I saw some innocent civilians get wounded by the drone operation that I was in charge of, we were able to foil the plot of a terrorist group and save many other lives).
"""

    )
    role_res = col2.text_area("", placeholder="Type here", key=84, max_chars=2000)

    submitted = st.form_submit_button("submit")


st.header(
        """ :blue[Exercise 10.6]
        Step 11: Talk to Someone You Trust
"""
)
with st.form("someone"):
    col1, col2 = st.columns(2)
    col1.write("When you feel hurt by someone's wrongdoing or experience a perpetration-type moral injury, do you typically seek out social support, or do you tend to handle it alone? Is there someone you trust enough to confide in about your genuine intention to cultivate greater forgiveness?")
    role_res = col2.text_area("", placeholder="Write that person’s, or persons’, name(s) here", key=85, max_chars=2000)


    col1, col2 = st.columns(2)
    col1.write("What are some reasons that you talk to that person? How do they typically respond to you? (Can you give others or yourself the same thing that person gives to you?)")
    role_res = col2.text_area("", placeholder="Type here", key=85.1, max_chars=2000)

    submitted = st.form_submit_button("submit")

st.header(
        """ :blue[Exercise 10.7]
        Step 12: Start a Campaign to Feel Warmth toward Yourself and/or “Enemies”
"""
)
with st.form("campaign"):
    col1, col2 = st.columns(2)
    col1.write("List actions you could undertake, both privately and publicly, to demonstrate the transformation in your feelings towards yourself or those who have caused you harm. Outline specific gestures you could make to exhibit the warmth of your emotions towards one of the individuals you identified in Step 2. Alternatively, describe some ways that you could more positively think about yourself after the realization that you have experienced a moral injury.")
    role_res = col2.text_area("", placeholder="Type here", key=86, max_chars=2000)

    st.write("You are now finished with the 12-step two-lesson exercises to help you become a more forgiving person. ")

    submitted = st.form_submit_button("submit")

st.header(
        """ :blue[Exercise 10.8]
        Freeing Yourself from the Burden of Unforgiveness
"""
)
st.write(
    """Let's take a moment to revisit something important. Throughout this journey, you've pondered the choice of fully forgiving yourself or the individual who caused you pain. Along the way, you've not only recognized the benefits of forgiveness but also experienced genuine emotional shifts as you considered a more objective perspective. Your empathy towards them or the situation and yourself has deepened, and you've witnessed how emotional forgiveness can enhance your own character. Moreover, you've reflected extensively on how to refine your forgiveness skills.

Now, here's a final opportunity to commit to complete forgiveness. With these thoughts in mind, clasp your hands and extend your arms outward as far as possible. Visualize the weight of hurt and unforgiveness resting in your hands. Hold onto this burden for about thirty seconds. As your arms begin to tire, contemplate all the other things you could be doing with your hands—and with your life—if you could release any lingering unforgiveness and move forward. Remember, holding onto this burden only harms you. However, letting go benefits you.

If you feel prepared to release and genuinely forgive, open your hands and allow your arms to return to their natural position. Experience the relief of that burden lifting from you. Understand that now, having forgiven, you can fully immerse yourself back into your life.

"""
)

st.header(
        """ :blue[Exercise 10.9]
        What Now?
"""
)
st.write(
    """Take a moment to assess whether you feel the need to dedicate additional time to either forgiving the hurt you've been focusing on or striving to cultivate a more forgiving disposition. Keep in mind: the depth of your forgiveness correlates with the sincerity and effort you invest in forgiving yourself and others. To aid in your decision-making process regarding whether to invest more time in forgiveness, engage in the following exercises, evaluating your experience with the workbook and tracking any changes in your forgiveness scores.
"""
)

st.header(
        """ :blue[Exercise 10.10]
        Knowledge Assessment
"""
)
st.write("Throughout this lesson, you've focused on forgiving a specific hurt. Across Lessons 1 to 8, you made strides in forgiving this hurt to varying degrees. In Lessons 9 and 10, you aimed to further develop your capacity for forgiveness. Now, with the foundation of having forgiven one hurt, you can extend the BREACH/PREACH forgiveness method to address other hurts. This process will underscore your practice of forgiveness and highlight your growth as a more forgiving individual.")
with st.form("know_10"):
    col1, col2 = st.columns(2)
    col1.write("Think back through this workbook. Write about the most important thing you have learned so far.")
    role_res = col2.text_area("", placeholder="Type here", key=87, max_chars=2000)

    submitted = st.form_submit_button("submit")

st.divider()

st.header(
        """ :blue[Lesson 11]
        Processing the Entire Workbook
"""
)
st.write(
    """Lessons You Can Remember
In the following 4 exercises, you will notice 4 lessons or perspectives—from a pencil, a mirror, a bodybuilder, and a scientist.

"""
)

st.header(
        """ :blue[Exercise 11.1]
        Learn From a Pencil 
"""
)
st.write(
    """Imagine a pencil with an eraser. Consider the following lesson for your life. 

•	A pencil, though short-lived, possesses the capacity to leave a lasting impression, much like you.

•	Unlike a pen, it allows for correction of mistakes through dedicated effort, sometimes requiring the unconventional act of standing it on its eraser. In a world that emphasizes the pursuit of power, prioritize love; opt for forgiveness over revenge and/or self-hate, for therein lies true strength.

•	Similar to you, the essence of the pencil, not its outward appearance, determines its ability to make a mark.

•	Regular sharpening is essential for its effectiveness, so embrace the process of honing yourself, as the challenges you face often serve as opportunities for growth and refinement.
"""
)

st.header(
        """ :blue[Exercise 11.2]
        Learn From a Mirror 
"""
)
st.write(
    """Peer into the mirror, then step back. Return to your reflection once more. You've beheld two sides of yourself. The first reflects a warrior who has faced both the turmoil of battle, the aftermath of conflict, and potentially moral wounds. The second embodies the resolve to confront the burdens of unforgiveness, the desire for retribution, and the weight of lingering resentments. It is the face of a soldier who has conquered the grip of unforgiveness – a hero of forgiveness. These faces both belong to you. Embrace the mantle of the forgiveness champion that resides within, and live out your days as a beacon of resilience and reconciliation.
""")

st.header(
        """ :blue[Exercise 11.3]
        Learn From a Bodybuilder 
"""
)
st.write(
    """Stand before that mirror once more, and tighten your bicep. Transitioning into a more forgiving individual can mirror the journey of fortifying your physical strength. You won't achieve muscle growth without effort and dedication, akin to the commitment you've shown in your future or previous military service. Just as strength training yields numerous benefits beyond physical prowess, forgiveness training carries far-reaching rewards beyond simply becoming more forgiving.
"""
)

st.header(
        """ :blue[Exercise 11.4]
        Learn From a Scientist 
"""
)
st.write(
    """Over 3000 scholarly papers have examined the concept of forgiveness. What have researchers discovered? Learn these lessons.

•	Every transgression holds the potential for forgiveness, though significant wrongs may necessitate a more extensive process.

•	With unwavering dedication, any offense can be forgiven.

•	Forgiveness often demands patience and persistent effort, especially when addressing particular grievances.

•	Embracing forgiveness fosters inner peace, psychological equilibrium, and enhanced physical well-being.

•	Cultivating forgiveness facilitates the cultivation of healthier, more fulfilling relationships and a view of ones self.

•	Engaging in forgiveness practices enriches one's spiritual journey.

"""
)

st.header(
        """ :blue[Exercise 11.5]
        Evaluate How Much You Have Learned about Forgiveness 
"""
)
st.write(
    """Rate how much you experienced each of the following statements on a scale of 1 to 5. Use a color to highlight, or circle with a pen, the rating for each item.
:green[1 = Not at all, 2 = A Little, 3 = Moderate, 4 = A Lot, 5 = Tremendous Amount]
"""
)

with st.form("Evaluate_11"):
    col1, col2 = st.columns(2)
    col1.write("I learned that deciding to forgive doesn’t always mean I have forgiven emotionally.")
    role_res = col2.radio('Pick one:', [1, 2, 3, 4, 5], index=None, horizontal=True, key=88)

    col1, col2 = st.columns(2)
    col1.write("I came to see the wrongdoer as more “human,” flawed, and needy than I did before.")
    role_res = col2.radio('Pick one:', [1, 2, 3, 4, 5], index=None, horizontal=True, key=89)

    col1, col2 = st.columns(2)
    col1.write("I understand the wrongdoer better now.")
    role_res = col2.radio('Pick one:', [1, 2, 3, 4, 5], index=None, horizontal=True, key=90)

    col1, col2 = st.columns(2)
    col1.write("I don’t see myself as so perfect as I did. I am capable of hurting other people.")
    role_res = col2.radio('Pick one:', [1, 2, 3, 4, 5], index=None, horizontal=True, key=91)

    col1, col2 = st.columns(2)
    col1.write(
        """I learned the 6 steps and can tell you what each is (5=correctly naming all 6):
B/P = ---, R = ---, E = ---, A = ---, C = ---, H = ---

"""
    )
    role_res = col2.radio('Pick one:', [1, 2, 3, 4, 5], index=None, horizontal=True, key=92)

    col1, col2 = st.columns(2)
    col1.write("If I start to worry about an old hurt, I have at least two things I could do to snap myself out of it and hold on to forgiveness.")
    role_res = col2.radio('Pick one:', [1, 2, 3, 4, 5], index=None, horizontal=True, key=93)

    col1, col2 = st.columns(2)
    col1.write("I have committed to being a more forgiving person because of the workbook.")
    role_res = col2.radio('Pick one:', [1, 2, 3, 4, 5], index=None, horizontal=True, key=94)

    col1, col2 = st.columns(2)
    col1.write("I have learned how I can be a more forgiving person.")
    role_res = col2.radio('Pick one:', [1, 2, 3, 4, 5,], index=None, horizontal=True, key=95)
    
    
    submitted = st.form_submit_button("submit")


st.header(
        """ :blue[Exercise 11.6]
        Knowledge Assessment 
"""
)
st.write(
    """
    In lesson 11, you are beginning to experience the internalization of forgiveness. Check your knowledge: imagine that you had to give a speech to a class of 13- to 15-year old students. Can you explain the following?

•	The advantages of forgiving

•	What an injustice gap is and how an apology from the wrongdoer makes the gap smaller and forgiveness likelier

•	What decisional forgiveness is

•	What emotional forgiveness is

•	What the 6 steps to BREACH/PREACH forgiveness are

•	An illustration from your life of how you used BREACH/PREACH forgiveness to forgive something.

•	An illustration from someone else’s life that inspires people to forgive.

"""
)

st.header(
        """ :blue[Lesson 12]
        Evaluating How Far You Have Come
"""
)
st.write("At the beginning of these 12 lessons, you conducted an evaluation of yourself. Let’s reconsider where you are at.")

st.header(
        """ :blue[Exercise 12.1]
        Rate (Again) Your Usual Use of Forgiveness  
"""
)
with st.form("Evaluate_12.1"):
    col1, col2 = st.columns(2)
    col1.write("You first rated your usual use of forgiveness (Exercise 1.1) from 0 (not at all) to 10 (completely). How would you rate your overall ability to forgive now?")
    role_res = col2.radio('Pick a number 0 to 10 ', [1, 2, 3, 4, 5, 6, 7, 8, 9, 10], index=None, horizontal=True, key=96)

    submitted = st.form_submit_button("submit")

st.header(
        """ :blue[Exercise 12.2]
        Consider (Again) the Hurt You Worked on
"""
)
st.write("You then chose a specific hurt to work on throughout this workbook (Exercise 1.2). You have spent approximately 2 hours working to forgive that hurt. You have also learned a lot about forgiveness in general. ")

st.header(
        """ :blue[Exercise 12.3]
        Rate (Again) Your Decision to Forgive the Hurt
"""
)
with st.form("Decision_12"):
    col1, col2 = st.columns(2)
    col1.write("You then rated your decisional forgiveness from 0 to 10 (Exercise 1.3), complete decision to forgive. How would you rate your decision to forgive now?")
    role_res = col2.radio('Pick a number 0 to 10 ', [1, 2, 3, 4, 5, 6, 7, 8, 9, 10], index=None, horizontal=True, key=97)

    submitted = st.form_submit_button("submit")

st.header(
        """ :blue[Exercise 12.4]
        Rate (Again) Your Emotional Forgiveness
"""
)
with st.form("Again_12"):
    col1, col2 = st.columns(2)
    col1.write("You also rated your emotional forgiveness from 0 (no emotional forgiveness) to 10 (complete emotional forgiveness) (Exercise 1.4). How would you rate your emotional forgiveness now? ")
    role_res = col2.radio('Pick a number 0 to 10 ', [1, 2, 3, 4, 5, 6, 7, 8, 9, 10], index=None, horizontal=True, key=98)

    submitted = st.form_submit_button("submit")

st.header(
        """ :blue[Exercise 12.5]
        Rate (Again) What You Learned
"""
)
st.write(
    """We trust you've gained valuable insights into the practice of forgiveness. Our hope extends to witnessing your effective application of forgiveness toward the wounds you've chosen to address, as well as those that may arise in your journey toward greater forgiveness.

In dedicating just a few hours to the process, you've made significant strides. Moreover, you now possess a readily accessible tool to utilize when feelings of anger, bitterness, or resentment arise toward yourself or anyone in your life. You can always return to this workbook to navigate through new instances of hurt.

"""
)

st.header(
        """ :blue[Exercise 12.6]
        How Long Did You Spend?
"""
)

st.write(" :blue[About how long, in hours and minutes, would you estimate that you spent on this workbook from start to finish?]")
with st.form("Time_used"):
    time = st.time_input("Time:")
    signature = st.text_input("Your Signature:(Name)")

    st.markdown(f"I AFFIRM THAT IT TOOK ME ABOUT **{time}**")
    st.markdown(f"SIGNED **{signature}**")

    submitted = st.form_submit_button("submit")


st.header(
        """ :blue[Exercise 12.7]
        Feedback
"""
)
with st.form("feedback"):
    col1, col2 = st.columns(2)
    col1.write("What feedback would you like to give the writer of this workbook?")
    role_res = col2.text_area("", placeholder="Type here", key=99, max_chars=2000)

    col1, col2 = st.columns(2)
    col1.write("What is the likelihood you’ll use this workbook again? (from 0% to 100%) ")
    role_res = col2.slider('Slide me', min_value=0, max_value=100)

    submitted = st.form_submit_button("submit")

