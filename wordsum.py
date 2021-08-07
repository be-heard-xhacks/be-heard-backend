# from transformers import AutoTokenizer, AutoModelForSeq2SeqLM
# from route_config import *

# # initializing tokenizer and model
# # store this somewhere else??
# tokenizer = AutoTokenizer.from_pretrained("sshleifer/distilbart-cnn-12-6")
# model = AutoModelForSeq2SeqLM.from_pretrained("sshleifer/distilbart-cnn-12-6")

# @app.route("/testmodel", methods = ["POST"])
# def summarize():
#     article = request.args.get("article")
#     inputs = tokenizer([article], return_tensors='pt')
#     summary_ids = model.generate(inputs['input_ids'], num_beams=4, early_stopping=True) # can set max_length (word count)
#     return jsonify({"msg": [tokenizer.decode(g, skip_special_tokens=True, clean_up_tokenization_spaces=False) for g in summary_ids]})


# # ARTICLE_TO_SUMMARIZE = "Women's Land Rights Agenda Share The Intergovernmental Authority on Development (IGAD) has endorsed the Regional Womens Land Rights Agenda in a bid to support the implementation of the AU Declaration on Land Issues and Challenges in Africa toward The Africa We Want and Leaving No One Behind. This is a culmination of the convention of the Ministerial meeting for the Ministers responsible for Land and Ministers responsible for Gender/Women Affairs in the IGAD member states, preceded by a Directors level meeting on July 26 and 27. To move the gender equality on land forward from a regional perspective, the Directors meeting will draw common threads from the National Womens Land Rights Agenda for the seven (7) Member States and the recommendations from the IGAD Regional Womens Land Rights Conference into the IGAD Region Womens Land Rights Agenda. The Regional Womens Land Rights Agenda is a framework document that will enable the IGAD Secretariat to provide the necessary support to the Member States in implementing gender and land projects for the next 10 years. Cabinet Secretary in the Ministry of Lands Farida Karoney said the AU Framework and Guidelines for land policy in Africa calls for individual member states to cooperate at regional levels to address land issues and challenges through comprehensive people-driven land policies and reforms in which womens rights to land are ingrained. Ministry of Lands and Physical Planning, in collaboration with IGAD, has held consultative meetings with key stakeholders to draw out Kenya Womens Land Rights Agenda. Consensus building has been done on outstanding Women Land Rights challenges and prioritization of the key issues. She said The IGAD Regional Womens Land Rights Agenda is operational, enabling the implementation of Gender Equality programs on land by the IGAD Secretariat and its IGAD Member States; Kenya, Uganda, Sudan, South Sudan, Djibouti, Somalia, and Ethiopia. A Communiqu was issued at the closing of the ministerial meeting. IGAD on 28 30 June 2021 held its first-ever Regional Womens Land Rights Conference that brought to bear the transnational and intergenerational connectedness of womens rights to land. Statements of commitment were received from the highest representatives of Government in the Ministries responsible for Lands and the Ministries responsible for Gender/Women Affairs of each of the IGAD Member States. The AU Declaration on Land Issues and Challenges gives a mandate to IGAD to provide technical guidance to the member countries, monitor land sectors progress, and promote regional land policy harmonization and womens land rights. The same Declaration gives a mandate to member states to promote land sector interventions that tackle underlying causes of tenure insecurity including securing and protecting all tenure rights, increasing transparency in land administration, and promoting equal access to land for all land users. It is on this basis that IGAD, through the IGAD Land Unit has worked on progressively crafting a strategic framework for its operations. The starting point was to help Member states assess common and shared land tenure challenges. For Gender Equality on land, the work commenced in 2020 with conducting gender assessments of the land sector in each of the IGAD Member States, with the aim of identification not only of issues for national attention but the transnational land governance issues and draw recommendations that strengthen regional integration through convergence. Share Subscribe to our newsletter and stay updated on the latest developments. previous post"

# # "Former Cardinal Theodore McCarrick, who was defrocked by The Vatican in 2019 over sex abuse allegations, is now facing criminal charges in Massachusetts for alleged sex abuse of a minor nearly 50 years ago, according to a court filing. According to a criminal complaint filed Wednesday, McCarrick is charged with three counts of indecent assault and battery on a person over 14. The complaint was filed by Wellesley Police in Dedham District Court. The Boston Globe was the first to report the charges. The filing states that the unnamed victim told investigators via Zoom in January that McCarrick had been friends with a family member and outlined multiple incidents of alleged abuse by McCarrick, most of which took place outside of Massachusetts in New Jersey, New York and California. One incident took place in Wellesley, Massachusetts, in June 1974 at the victim's brother's wedding, where the victim said McCarrick allegedly pulled him aside and told him, 'Your dad wants you to come with me and have a talk. You're being mischievous at home and not attending church. We need to go outside and have a conversation,' according to the complaint. The victim told investigators McCarrick told the victim to take down his pants and then held and 'kissed' his genitalia 'saying prayers to make me feel holy,' according to the complaint. After telling him to pull up his pants, McCarrick allegedly told the boy to say certain prayers 'so God can redeem you of your sins.' The complaint states that the victim told investigators that McCarrick repeatedly sexually abused him over the years, including when he was an adult, with abuse that also allegedly took place in nearby Newton, Massachusetts when he was older. The complaint states that the victim told investigators that McCarrick repeatedly sexually abused him over the years, including when he was an adult, with abuse that took place in nearby Newton, Massachusetts, when he was older. The criminal charges make McCarrick the highest-ranking Catholic official in the US to face criminal charges for sex abuse of a minor, according to the unnamed victim's attorney, Mitchell Garabedian. 'Historically, this is the first time ever in the United States that a Cardinal has been criminally charged with a sexual crime against a minor,' Garabedian said in a news release. 'It takes an enormous amount of courage for a sexual abuse victim to report having been sexually abused to investigators and proceed through the criminal process.' Barry Coburn, an attorney for McCarrick, told CNN in a statement, 'We are going to address this issue in the courtroom.' McCarrick has maintained his innocence in the past regarding previous allegations. Raised to cardinal in 2001 by John Paul, a year after he became Archbishop of Washington, McCarrick went on to become a power player both in the Church and in Washington, DC, and was known for his fundraising and influence overseas. He resigned from the College of Cardinals in 2018 and was defrocked by the Vatican in 2019 after a Church trial found him guilty of sexually abusing minors. McCarrick has been issued a summons ordering him to appear in court for an arraignment on August 26, according to the filing. CNN has reached out to the Wellesley Police Department, the Norfolk County District Attorney's Office and The Vatican for a comment. This is only the third high-ranking member of the Catholic church in the US to be criminally charged with crimes related to sex abuse, said Marci Hamilton, CEO of Child USA, who has worked with hundreds of victims of sex abuse at the hands of priests and clergy. 'When prosecutors bring charges against the powerful in a religious institution like the Catholic church they are validating the thousands of victims that have come forward,' Hamilton told CNN. 'In the state of Massachusetts for prosecutors to file these charges against a powerful member of the church shows that the child sex abuse movement is making inroads and it heartens me.' In the court filing, investigators wrote that the January interview with the victim took place in response to a letter sent to the Middlesex District Attorney's Office by Garabedian. Meghan Kelly, a spokeswoman for the Middlesex District Attorney's Office told CNN, 'our investigation remains ongoing at this time.''"



# # [' Former Cardinal Theodore McCarrick is charged with three counts of indecent assault and battery on a person over 14 . The unnamed victim told investigators via Zoom in January that he was friends with a family member and outlined multiple incidents of alleged abuse . Most of the alleged abuse took place outside of Massachusetts in New Jersey, New York and California . The complaint states that the victim was sexually abused over the years, including when he was an adult, with abuse that also allegedly took place in nearby Newton, Massachusetts .']