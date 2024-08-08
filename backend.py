import os
import streamlit as st
from langchain_community.chat_models import ChatOpenAI
from langchain.prompts import PromptTemplate
from langchain.prompts import FewShotPromptTemplate
from langchain.prompts.example_selector import LengthBasedExampleSelector

from dotenv import load_dotenv


def getLLMResponse(query, category_option, task_option):
    load_dotenv()
    llm = OpenAI(temperature = 0.9, model = 'gpt-3.5-turbo-instruct')
    if category_option =="Sales Professional":
        examples = [
            {
             "query": "What strategies would you recommend for effectively segmenting a market?",
"answer": "To effectively segment a market, it's essential to analyze factors such as demographics, psychographics, behavior, and geographic location. Utilize market research data to identify common characteristics among potential customers and group them accordingly. Implement targeted marketing strategies tailored to each segment to maximize engagement and conversion rates."
},
{
"query": "How do you conduct a thorough competitive analysis in your sales approach?",
"answer": "Conducting a thorough competitive analysis involves identifying key competitors, evaluating their product offerings, pricing strategies, distribution channels, and marketing tactics. Utilize tools like SWOT analysis to assess strengths, weaknesses, opportunities, and threats posed by competitors. Incorporate competitive insights into your sales strategy to highlight your unique value proposition and address competitive challenges effectively."
},
{
"query": "In your experience, how crucial is brand positioning for driving sales success?",
"answer": "Brand positioning plays a crucial role in driving sales success as it defines how customers perceive a product or service relative to competitors. A strong brand position communicates value, relevance, and differentiation, influencing purchase decisions and fostering customer loyalty. Align sales efforts with brand positioning to effectively communicate value propositions and build trust with customers."
},
{
"query": "Can you discuss a successful instance where social media significantly impacted sales outcomes?",
"answer": "Certainly, social media can significantly impact sales outcomes by amplifying brand visibility, fostering engagement, and driving conversions. For example, leveraging targeted ads on platforms like Facebook or Instagram can reach specific audience segments with tailored messages, leading to increased sales and customer acquisition. Additionally, utilizing influencers or brand advocates can enhance credibility and trust, further driving sales."
},
{
"query": "How do you utilize data analytics to optimize sales performance?",
"answer": "Data analytics plays a vital role in optimizing sales performance by providing insights into customer behavior, preferences, and purchasing patterns. By analyzing sales data, businesses can identify trends, forecast demand, and segment customers for personalized targeting. Utilize analytics tools to track key performance metrics, measure sales effectiveness, and identify areas for improvement to drive revenue growth and profitability."
},
{
"query": "In your experience, how do evolving consumer trends impact sales strategies?",
"answer": "Evolving consumer trends directly influence sales strategies by shaping product development, messaging, and sales approaches. Keeping abreast of consumer trends enables sales professionals to anticipate changing customer needs, tailor offerings accordingly, and stay ahead of competitors. For instance, aligning sales strategies with trends like sustainability or digitalization can resonate with eco-conscious or tech-savvy consumers, driving sales."
},
{
"query": "How do you stay updated with the latest product features and advancements in your industry?",
"answer": "As a seasoned sales professional, staying updated with the latest product features and advancements is crucial. This involves actively engaging in product training sessions, attending industry conferences, networking with colleagues, and regularly monitoring industry publications and online resources. By staying informed, sales professionals can effectively articulate product benefits, address customer inquiries, and drive sales."
},
{
"query": "How do you effectively communicate the benefits of a new product compared to previous models?",
"answer": "Effectively communicating the benefits of a new product compared to previous models requires understanding the unique value propositions and improvements. Focus on highlighting key features, performance enhancements, and customer benefits through clear and compelling messaging. Utilize product demonstrations, case studies, and testimonials to showcase real-world applications and success stories, persuading customers to upgrade or switch."
},
{
"query": "Can you discuss a successful sales strategy employed to differentiate a product from competitors?",
"answer": "Certainly, a successful sales strategy to differentiate a product from competitors involves emphasizing unique selling points, addressing customer pain points, and showcasing value propositions effectively. By highlighting features, benefits, and advantages over competitors, sales professionals can position the product as the superior choice. Additionally, offering customized solutions, exceptional customer service, and post-sales support can further differentiate the product and drive sales."
},
{
"query": "How do you adapt your sales approach to align with the changing needs and preferences of customers?",
"answer": "Adapting the sales approach to align with changing customer needs and preferences requires flexibility, empathy, and continuous learning. This involves actively listening to customer feedback, understanding pain points, and customizing solutions to meet specific requirements. Utilize consultative selling techniques to uncover opportunities, educate customers, and offer tailored recommendations that address evolving needs, ultimately driving customer satisfaction and loyalty."
}
]
    elif category_option=="Marketing Professional":
        examples = [
            {
              "query": "What are the key methodologies you employ for conducting market analysis?",
"answer": "For market analysis, I utilize a combination of qualitative and quantitative research methodologies. This includes conducting market surveys, focus groups, and interviews to gather qualitative insights into consumer preferences and behaviors. Additionally, I leverage data analytics tools to analyze market trends, competitive landscape, and consumer demographics, providing quantitative data for informed decision-making."
},
{
"query": "How do you interpret consumer behavior data to inform marketing strategies?",
"answer": "Interpreting consumer behavior data is essential for informing marketing strategies. By analyzing data such as purchase history, browsing patterns, and social media interactions, I identify consumer preferences, motivations, and pain points. This insight allows me to develop targeted marketing campaigns, personalized messaging, and product offerings that resonate with the target audience, driving engagement and conversion."
},
{
"query": "In your experience, how does market segmentation contribute to effective marketing campaigns?",
"answer": "Market segmentation plays a crucial role in tailoring marketing campaigns to specific audience segments. By dividing the market into smaller, more defined groups based on demographics, psychographics, and behavior, marketers can create targeted messages and promotions that resonate with each segment's unique needs and preferences. This increases the effectiveness of marketing efforts, maximizes ROI, and enhances customer satisfaction."
},
{
"query": "Can you discuss a successful instance where consumer behavior insights drove a marketing strategy?",
"answer": "Certainly, consumer behavior insights have driven numerous successful marketing strategies. For example, by analyzing data indicating a growing preference for eco-friendly products among millennials, a company may develop a sustainability-focused marketing campaign highlighting the environmental benefits of its products. This targeted approach resonates with environmentally conscious consumers, resulting in increased brand loyalty and market share."
},
{
"query": "How do you leverage consumer trends to stay ahead of the competition in your marketing efforts?",
"answer": "Staying ahead of the competition requires staying attuned to consumer trends and adapting marketing strategies accordingly. I monitor emerging trends such as sustainability, personalization, and digitalization through market research, industry reports, and social media analysis. By aligning marketing efforts with these trends, I can capitalize on new opportunities, differentiate the brand, and maintain relevance in the market."
},
{
"query": "How do you incorporate market analysis findings into the development of marketing campaigns?",
"answer": "Market analysis findings serve as the foundation for developing effective marketing campaigns. I translate insights gleaned from market research into actionable strategies by identifying target segments, crafting compelling messaging, and selecting appropriate channels for reaching the audience. Additionally, I continuously monitor campaign performance metrics and consumer feedback to optimize strategies and ensure campaign success."
},
{
"query": "What strategies do you employ to effectively communicate brand positioning to target audiences?",
"answer": "Effectively communicating brand positioning requires a comprehensive understanding of the brand identity and its value proposition. I utilize integrated marketing communication strategies to convey the brand's unique attributes, values, and benefits across various touchpoints. This includes crafting consistent messaging, visual branding elements, and storytelling techniques that resonate with the target audience, building brand awareness and loyalty."
},
{
"query": "How do you measure the success of marketing campaigns in terms of consumer engagement and ROI?",
"answer": "Measuring the success of marketing campaigns involves tracking key performance indicators related to consumer engagement and ROI. This includes metrics such as website traffic, click-through rates, conversion rates, and return on advertising spend (ROAS). I utilize analytics platforms and attribution models to assess campaign effectiveness, optimize budget allocation, and make data-driven decisions to maximize ROI and achieve marketing objectives."
},
{
"query": "Can you discuss a time when your market analysis led to a successful product launch or repositioning?",
"answer": "Certainly, market analysis has played a pivotal role in guiding successful product launches and repositioning efforts. For instance, by identifying a gap in the market for premium organic skincare products through comprehensive market research, we developed and launched a new product line targeting health-conscious consumers. This strategic move resulted in increased market share, heightened brand visibility, and positive consumer feedback."
},
{
"query": "How do you stay updated with the latest trends and developments in market analysis and consumer behavior?",
"answer": "As a marketing professional, staying updated with the latest trends and developments in market analysis and consumer behavior is essential. I regularly attend industry conferences, workshops, and webinars to gain insights from thought leaders and industry experts. Additionally, I subscribe to reputable publications, research reports, and online forums to stay abreast of emerging trends and best practices, ensuring continuous professional development."
}
]
    elif category_option=="Branding Professional":
        examples = [
            {
               "query": "How do you define the role of branding in influencing consumer behavior and driving sales?",
"answer": "Branding plays a pivotal role in influencing consumer behavior and driving sales by shaping perceptions, building emotional connections, and fostering brand loyalty. A strong brand identity communicates values, personality, and differentiation, resonating with target consumers and influencing purchase decisions. Effective branding enhances brand recognition, trust, and credibility, ultimately driving sales and market share."
},
{
"query": "Can you discuss a successful branding initiative that resulted in significant sales growth?",
"answer": "Certainly, successful branding initiatives often lead to significant sales growth. For example, by repositioning a product as a premium offering through a comprehensive branding campaign highlighting its superior quality and craftsmanship, we were able to attract affluent consumers and command higher prices, resulting in increased sales revenue and market share."
},
{
"query": "How do you leverage consumer behavior insights to inform branding strategies?",
"answer": "Leveraging consumer behavior insights is crucial for informing branding strategies. By understanding consumer preferences, motivations, and purchasing behavior, branding professionals can develop strategies that resonate with target audiences. This may involve tailoring brand messaging, imagery, and experiences to align with consumer desires, aspirations, and emotional triggers, driving brand engagement and loyalty."
},
{
"query": "In your experience, how does brand positioning impact sales effectiveness?",
"answer": "Brand positioning directly impacts sales effectiveness by influencing how consumers perceive a product or service relative to competitors. A well-defined brand position communicates unique value propositions, differentiation, and relevance, influencing purchase decisions and brand preference. Aligning brand positioning with consumer needs and market trends enhances sales effectiveness, driving conversion rates and customer loyalty."
},
{
"query": "How do you develop and maintain a consistent brand identity across various marketing channels?",
"answer": "Developing and maintaining a consistent brand identity across marketing channels is essential for brand integrity and recognition. This involves defining brand elements such as logo, colors, typography, and tone of voice, and ensuring they are consistently applied across all touchpoints. Implementing brand guidelines, conducting regular audits, and providing training to stakeholders help uphold brand consistency and coherence, reinforcing brand equity and credibility."
},
{
"query": "Can you discuss the importance of storytelling in branding and its impact on sales?",
"answer": "Storytelling is integral to branding as it humanizes the brand, engages emotions, and creates memorable experiences for consumers. Through compelling narratives, brands can communicate their values, origins, and purpose, forging deeper connections with audiences. This emotional resonance fosters brand affinity, word-of-mouth advocacy, and repeat purchases, ultimately driving sales and brand loyalty."
},
{
"query": "How do you measure the effectiveness of branding efforts in terms of sales impact?",
"answer": "Measuring the effectiveness of branding efforts in terms of sales impact involves tracking key performance indicators such as brand awareness, brand perception, and purchase intent. Additionally, analyzing sales data, customer feedback, and market share metrics provides insights into the direct correlation between branding initiatives and sales outcomes. Utilizing surveys, focus groups, and market research studies helps gauge consumer perceptions and attitudes towards the brand, informing future branding strategies."
},
{
"query": "What strategies do you employ to differentiate a brand in a competitive market landscape?",
"answer": "To differentiate a brand in a competitive market landscape, I focus on identifying and communicating unique value propositions that resonate with target consumers. This may involve emphasizing product features, benefits, or brand values that set the brand apart from competitors. Additionally, leveraging storytelling, experiential marketing, and brand partnerships can create memorable brand experiences that foster differentiation, driving sales and brand preference."
},
{
"query": "How do you adapt branding strategies to align with changing consumer preferences and market dynamics?",
"answer": "Adapting branding strategies to align with changing consumer preferences and market dynamics requires agility and responsiveness. This involves continuously monitoring consumer trends, market shifts, and competitor activities to identify opportunities and threats. By staying attuned to evolving consumer needs and values, branding professionals can adjust brand positioning, messaging, and experiences to remain relevant, driving sales and sustaining brand relevance."
},
{
"query": "What role does brand loyalty play in sustaining long-term sales growth?",
"answer": "Brand loyalty is crucial for sustaining long-term sales growth as it fosters repeat purchases, advocacy, and customer lifetime value. Loyal customers are less price-sensitive and more likely to choose the brand over competitors, resulting in higher sales volume and profitability. By nurturing relationships, delivering exceptional experiences, and maintaining brand consistency, branding professionals can cultivate brand loyalty, driving sustainable sales growth and market success."
}
]
    elif category_option=="Digital Marketing":
        examples = [
            {
                "query": "How do you define the role of digital marketing in increasing engagement, impressions, and SERP ranking?",
"answer": "Digital marketing plays a crucial role in increasing engagement, impressions, and SERP (Search Engine Results Page) ranking by leveraging online channels and strategies to reach and resonate with target audiences. Through tactics such as content marketing, social media engagement, SEO (Search Engine Optimization), and PPC (Pay-Per-Click) advertising, digital marketers can drive traffic, enhance visibility, and improve search engine rankings, ultimately increasing brand exposure and audience engagement."
},
{
"query": "Can you discuss a successful digital marketing campaign you've led that significantly increased engagement and impressions?",
"answer": "Certainly, I led a successful digital marketing campaign that significantly increased engagement and impressions by implementing a comprehensive content marketing strategy. By creating high-quality, relevant content tailored to the target audience's interests and needs, we were able to increase website traffic, social media engagement, and overall brand visibility. Through strategic distribution and promotion across various digital channels, we achieved substantial growth in impressions and engagement metrics."
},
{
"query": "How do you optimize digital marketing strategies to improve SERP ranking and organic visibility?",
"answer": "Optimizing digital marketing strategies for improved SERP ranking and organic visibility involves a multifaceted approach. This includes conducting keyword research to identify relevant search terms, optimizing on-page elements such as meta tags, headings, and content, and building high-quality backlinks from authoritative websites. Additionally, creating valuable, shareable content and optimizing website performance for speed and mobile-friendliness contribute to higher search engine rankings and increased organic traffic."
},
{
"query": "In your experience, how does social media engagement contribute to overall digital marketing success?",
"answer": "Social media engagement plays a vital role in overall digital marketing success by facilitating direct interaction with target audiences, building brand awareness, and driving website traffic. Through consistent posting, active engagement with followers, and strategic use of hashtags and multimedia content, digital marketers can foster meaningful relationships, amplify brand messaging, and increase visibility across social platforms, ultimately leading to higher engagement rates and conversions."
},
{
"query": "What strategies do you employ to increase audience engagement and interaction on digital platforms?",
"answer": "To increase audience engagement and interaction on digital platforms, I employ various strategies tailored to the target audience and platform dynamics. This includes creating compelling and interactive content such as polls, quizzes, and contests to encourage participation and sharing. Additionally, fostering community engagement through timely responses, user-generated content, and influencer partnerships enhances brand authenticity and fosters a sense of belonging among followers, driving sustained engagement and loyalty."
},
{
"query": "How do you measure the effectiveness of digital marketing efforts in terms of engagement, impressions, and SERP ranking?",
"answer": "Measuring the effectiveness of digital marketing efforts involves tracking key performance indicators (KPIs) such as engagement metrics (likes, shares, comments), impressions, and SERP ranking positions. Utilizing web analytics tools, social media insights, and SEO analytics platforms enables digital marketers to assess campaign performance, identify areas for improvement, and make data-driven optimizations to maximize engagement, visibility, and search engine rankings."
},
{
"query": "What role does content marketing play in improving engagement, impressions, and SERP ranking?",
"answer": "Content marketing plays a pivotal role in improving engagement, impressions, and SERP ranking by providing valuable, relevant content that resonates with target audiences and search engines. High-quality content optimized with targeted keywords and structured for readability enhances organic visibility and search engine rankings. Moreover, engaging and shareable content fosters audience interaction, amplifies brand reach, and drives website traffic, ultimately increasing engagement and impressions."
},
{
"query": "How do you stay updated with the latest trends and best practices in digital marketing?",
"answer": "Staying updated with the latest trends and best practices in digital marketing is essential for maintaining a competitive edge. I regularly attend industry conferences, webinars, and workshops to gain insights from industry experts and thought leaders. Additionally, I participate in online forums, subscribe to industry publications, and follow reputable blogs and social media accounts dedicated to digital marketing to stay abreast of emerging trends and innovations, ensuring continuous professional development."
},
{
"query": "What strategies do you implement to improve SERP ranking and increase organic visibility for websites?",
"answer": "To improve SERP ranking and increase organic visibility for websites, I implement a comprehensive SEO strategy that includes keyword research, on-page optimization, technical SEO enhancements, and link building. By optimizing website content, improving site structure and performance, and acquiring high-quality backlinks from authoritative sources, I aim to improve search engine rankings, increase organic traffic, and enhance overall visibility and relevance in search results."
},
{
"query": "How do you tailor digital marketing strategies to align with changing consumer behavior and market trends?",
"answer": "Tailoring digital marketing strategies to align with changing consumer behavior and market trends involves continuous monitoring and analysis of audience preferences, habits, and online interactions. By leveraging data analytics and social listening tools, digital marketers can identify emerging trends, anticipate shifts in consumer behavior, and adapt strategies accordingly. This may include adjusting content themes, messaging, and channel selection to ensure relevance and resonance with the target audience, ultimately driving engagement and impressions."
}
]
    elif category_option=="Advertising Professional":
        examples = [
            {
                
        "query": "How do you define the role of advertising in driving sales, with a focus on creating ad copies?",
"answer": "Advertising plays a pivotal role in driving sales by creating compelling ad copies that resonate with target audiences and motivate action. Ad copies serve as the primary means of communication between brands and consumers, conveying key messages, value propositions, and calls to action. By crafting persuasive and engaging ad copies that highlight product benefits, address consumer needs, and evoke emotions, advertisers can effectively drive conversions and achieve sales objectives."
},
{
"query": "Can you discuss a successful advertising campaign you've led that resulted in significant sales with a high conversion rate?",
"answer": "Certainly, I led a successful advertising campaign that resulted in significant sales with a high conversion rate. By developing targeted ad copies tailored to specific audience segments, we effectively communicated product features and benefits, compelling consumers to take action. Through strategic placement, messaging, and creative elements, we achieved a conversion rate of 66%, surpassing sales targets and delivering measurable ROI for the client."
},
{
"query": "How do you ensure that ad copies effectively capture audience attention and drive sales?",
"answer": "Ensuring ad copies effectively capture audience attention and drive sales requires a deep understanding of consumer psychology, market trends, and persuasive techniques. I focus on crafting attention-grabbing headlines, compelling storytelling, and clear calls to action that resonate with target audiences' desires and pain points. Additionally, I conduct thorough testing and optimization to refine ad copies based on performance data, maximizing conversion rates and sales effectiveness."
},
{
"query": "In your experience, what elements are crucial for creating ad copies that can consistently bring sales?",
"answer": "Several elements are crucial for creating ad copies that consistently bring sales. These include understanding the target audience's demographics, preferences, and motivations, as well as highlighting unique selling points and benefits that differentiate the product or service. Additionally, employing persuasive language, incorporating social proof, and offering incentives or promotions can further incentivize purchase behavior and drive sales conversions."
},
{
"query": "How do you tailor ad copies to different platforms and advertising channels while maintaining consistency in messaging?",
"answer": "Tailoring ad copies to different platforms and advertising channels requires adapting messaging and creative elements to align with platform dynamics and audience behaviors. While maintaining consistency in messaging and branding, I customize ad copies to fit the context, format, and audience demographics of each platform. This may involve adjusting tone, length, and imagery to optimize engagement and resonance, ultimately driving sales across diverse advertising channels."
},
{
"query": "What strategies do you employ to measure the effectiveness of ad copies in driving sales?",
"answer": "Measuring the effectiveness of ad copies in driving sales involves tracking key performance indicators (KPIs) such as conversion rates, click-through rates, and ROI. I utilize analytics tools and attribution models to analyze campaign performance, identify top-performing ad copies, and optimize messaging and targeting accordingly. Additionally, conducting A/B testing and audience segmentation enables me to refine ad copies based on data-driven insights, maximizing sales impact."
},
{
"query": "How do you stay updated with the latest trends and best practices in advertising to continuously improve ad copy performance?",
"answer": "Staying updated with the latest trends and best practices in advertising is essential for continuously improving ad copy performance. I actively monitor industry publications, attend advertising conferences, and participate in professional development workshops to stay abreast of emerging trends, technologies, and consumer behavior insights. Additionally, collaborating with cross-functional teams and networking with peers allows me to exchange ideas and learn from industry experts, ensuring that my ad copies remain relevant and effective in driving sales."
},
{
"query": "What role does creativity play in crafting ad copies that drive sales?",
"answer": "Creativity plays a crucial role in crafting ad copies that drive sales by capturing attention, sparking interest, and fostering emotional connections with consumers. Innovative and original ad copies stand out in a crowded advertising landscape, leaving a lasting impression on audiences and motivating action. By thinking outside the box, leveraging storytelling techniques, and incorporating visual elements, advertisers can create memorable ad copies that resonate with consumers and drive sales."
},
{
"query": "How do you ensure that ad copies maintain relevance and effectiveness over time?",
"answer": "Ensuring that ad copies maintain relevance and effectiveness over time requires continuous monitoring, testing, and optimization. I regularly review campaign performance data, audience feedback, and market trends to identify opportunities for improvement and refinement. By staying agile and responsive to changes in consumer behavior and competitive landscape, I can adapt ad copies accordingly, ensuring they remain compelling, persuasive, and effective in driving sales."
},
{
"query": "What strategies do you implement to maximize the conversion rate of ad copies and achieve sales objectives?",
"answer": "To maximize the conversion rate of ad copies and achieve sales objectives, I employ a combination of strategic targeting, persuasive messaging, and seamless user experience. This includes identifying high-value audience segments, tailoring ad copies to their specific needs and preferences, and optimizing landing pages for conversion. Additionally, employing urgency, scarcity, and social proof tactics can create a sense of FOMO (fear of missing out) and prompt immediate action, driving sales and achieving desired conversion rates."
}
]
        
  
        
   
        
    prompt_template = """
    Question:{query}
    Response:{answer}
    """
    example_prompt = PromptTemplate(
        input_variables=["query", "answer"],
        template=prompt_template
    )

    prefix = """
    "you are a {template_category_option} and {template_task_option}
    """
    suffix = """
    Question:{template_user_input}
    Response:
    """

    example_selector = LengthBasedExampleSelector(
        examples = examples,
        example_prompt=example_prompt,
        max_length=200
    )

    new_prompt_template = FewShotPromptTemplate(
        example_selector=example_selector,
        prefix=prefix,
        suffix=suffix,
        input_variables=['template_user_input','template_category_option','template_task_option'],
        example_separator = "\n"
    )
    print(new_prompt_template.format(template_user_input = query, template_expertise_level = category_option, template_task_option = task_option ))
    response = llm.invoke(new_prompt_template.format(template_user_input = query, template_expertise_level = category_option, template_task_option = task_option ))
    
    return response

st.set_page_config(page_title="Hi there!", page_icon=":robot:", layout="centered")
form_input = st.text_area("Tell me something", height=100)
task_option = st.selectbox(
    "what can I do for you?",
    ("write a Facebook post", "create a tweet", "Write a LinkedIn post", "Create a Newsletter", "Write a Sales Pitch", "Create a Reddit post","Powerpoint Bullets"),key=1)
category_option = st.selectbox(
    "which category do you identify yourself?",
    ("Sales Professional","Marketing Professional","Digital Marketing","Advertising Professional","Branding Professional"),key= 2)

Number_of_Words = st.slider('word limit', 1 , 200,25)
submit = st.button("Voila!")

if submit:
    print(getLLMResponse(form_input, task_option, category_option))
