import ast
import string
import pandas as pd


# This function calls other functions that calculate the descriptive statistics and the one it prints them
def all_statistics(data, overall=False):

    total_number_of_speeches, total_number_of_paragraphs, total_number_of_words, avg_paragraphs_per_speech, avg_words_per_speech, avg_words_per_paragraph = general_statistics(data)

    agenda_percentage, criticism_percentage = agenda_statistics(data)

    sum_of_unique_topics_of_all_speeches, avg_of_unique_topics_of_per_speech = topic_statistics(data)

    sentiment_avg, sentiment_avg_per_speech, polarization_avg, polarization_avg_per_speech, populism_avg, populism_avg_per_speech = sentiment_polarization_populism_statistics(data)

    sum_of_unique_entities_of_all_speeches, average_unique_entities_per_speech, avg_of_unique_entities_per_paragraph = entities_statistics(data, overall)

    print_statistics(total_number_of_speeches, total_number_of_paragraphs, total_number_of_words, avg_paragraphs_per_speech, avg_words_per_speech, avg_words_per_paragraph, 
                     agenda_percentage, criticism_percentage, sum_of_unique_topics_of_all_speeches, avg_of_unique_topics_of_per_speech, sentiment_avg, 
                     sentiment_avg_per_speech, polarization_avg, polarization_avg_per_speech, populism_avg, populism_avg_per_speech, sum_of_unique_entities_of_all_speeches, 
                     average_unique_entities_per_speech, avg_of_unique_entities_per_paragraph)


# This function calculates the descritpive statistics of the metadata of the speeches
def general_statistics(data):
    total_number_of_speeches = len(data.groupby(['politician', 'date (YYYY-MM-DD)', 'location']).first().reset_index())
    total_number_of_paragraphs = len(data.groupby(['politician', 'date (YYYY-MM-DD)', 'location', 'paragraph']).size())
    total_number_of_words = data['text'].apply(lambda x: len(x.translate(str.maketrans('', '', string.punctuation)).strip().split())).sum()   
    avg_paragraphs_per_speech = round(total_number_of_paragraphs/total_number_of_speeches, 2)
    avg_words_per_speech = round(total_number_of_words/total_number_of_speeches, 2)
    avg_words_per_paragraph = round(total_number_of_words/total_number_of_paragraphs, 2)

    return total_number_of_speeches, total_number_of_paragraphs, total_number_of_words, avg_paragraphs_per_speech, avg_words_per_speech, avg_words_per_paragraph


# This function calculates the percentages of the paragraphs classified as 'political agenda' and 'criticism'
def agenda_statistics(data):
    percentages = data['criticism_or_agenda_human'].value_counts(normalize=True) 
    agenda_percentage = round(percentages.get(0), 4).item()
    criticism_percentage = round(percentages.get(1), 4).item()

    return agenda_percentage, criticism_percentage


# This function calculates the number of unique topics of all speeches and the average number of unique topics per speech
def topic_statistics(data):
    sum_of_unique_topics_of_all_speeches = data['topic_human'].nunique()
    avg_of_unique_topics_of_per_speech = round(data.groupby(['politician', 'date (YYYY-MM-DD)', 'location'])['topic_human'].nunique().mean(),2)

    return sum_of_unique_topics_of_all_speeches, avg_of_unique_topics_of_per_speech


# This function calculates the average sentiment, polarization and populism of all the speeches and the average of these values per speech
def sentiment_polarization_populism_statistics(data):
    sentiment_avg = round(data['sentiment_human'].mean(),2)
    sentiment_avg_per_speech = round(data.groupby(['politician', 'date (YYYY-MM-DD)', 'location'])['sentiment_human'].mean().mean(),2)

    polarization_avg = round(data['polarization_human'].mean(),2)
    polarization_avg_per_speech = round(data.groupby(['politician', 'date (YYYY-MM-DD)', 'location'])['polarization_human'].mean().mean(),2)

    populism_avg = round(data['populism_human'].mean(),2)
    populism_avg_per_speech = round(data.groupby(['politician', 'date (YYYY-MM-DD)', 'location'])['populism_human'].mean().mean(),2)

    return sentiment_avg, sentiment_avg_per_speech, polarization_avg, polarization_avg_per_speech, populism_avg, populism_avg_per_speech


# This function calculates the number of unique entities of all speeches, the average number of unique entities per speech and the average number of unique entities per paragraph
def unique_elements_of_different_lists(lists):
    all_elements = []
    for l in lists:
        all_elements.extend(l)
    return set(all_elements)
def entities_statistics(data, overall):
    if overall:
        data['entity_specific_human'] = data['entity_specific_human'].apply(lambda x: ast.literal_eval(x))
    data['unique_specific_entities_par'] = data['entity_specific_human'].apply(lambda x: set(x))
    speech_level_df = data.groupby(['politician', 'date (YYYY-MM-DD)', 'location'])
    result = speech_level_df['entity_specific_human'].agg(unique_elements_of_different_lists).reset_index()
    result.rename(columns={'entity_specific_human': 'unique_specific_entities_speech'}, inplace=True)
    data = pd.merge(data, result, on=['politician', 'date (YYYY-MM-DD)', 'location'], how='left')

    sum_of_unique_entities_of_all_speeches = len(set().union(*data['unique_specific_entities_speech']))
    grouped = data.groupby(['politician', 'date (YYYY-MM-DD)', 'location'])['unique_specific_entities_speech']
    unique_entities_per_speech = grouped.apply(lambda x: len(set().union(*x)))
    average_unique_entities_per_speech = round(unique_entities_per_speech.mean(),2)
    avg_of_unique_entities_per_paragraph = round(data['unique_specific_entities_par'].apply(lambda x: len(x)).mean(),2)

    return sum_of_unique_entities_of_all_speeches, average_unique_entities_per_speech, avg_of_unique_entities_per_paragraph


# This function prints the descriptive statistics
def print_statistics(total_number_of_speeches, total_number_of_paragraphs, total_number_of_words, avg_paragraphs_per_speech, avg_words_per_speech, avg_words_per_paragraph, 
                     agenda_percentage, criticism_percentage, sum_of_unique_topics_of_all_speeches, avg_of_unique_topics_of_per_speech, sentiment_avg, sentiment_avg_per_speech, 
                     polarization_avg, polarization_avg_per_speech, populism_avg, populism_avg_per_speech, sum_of_unique_entities_of_all_speeches, average_unique_entities_per_speech, 
                     avg_of_unique_entities_per_paragraph, ):
    
    print('General statistics:')
    print('-------------------')
    print('total number of speeches: ', total_number_of_speeches)
    print('total number of paragraphs: ', total_number_of_paragraphs)
    print('total number of words: ', total_number_of_words)
    print('avg paragraphs per speech: ', avg_paragraphs_per_speech)
    print('avg words per speech ', avg_words_per_speech)
    print('avg words per paragraph: ', avg_words_per_paragraph)

    print('Criticism vs agenda percentages:')
    print('--------------------------------')
    print('agenda percentage: ', agenda_percentage)
    print('criticism percentage: ', criticism_percentage)

    print('Topics statistics:')
    print('------------------')
    print('sum_of_unique_topics_of_all_speeches: ', sum_of_unique_topics_of_all_speeches)
    print('avg_of_unique_topics_of_per_speech: ', avg_of_unique_topics_of_per_speech)

    print('Sentiment, polarization and populsim statistics:')
    print('------------------------------------------------')
    print('sentiment_avg: ', sentiment_avg)
    print('sentiment_avg_per_speech: ', sentiment_avg_per_speech)
    print('polarization_avg: ', polarization_avg)
    print('polarization_avg_per_speech: ', polarization_avg_per_speech)
    print('populism_avg: ', populism_avg)
    print('populism_avg_per_speech: ', populism_avg_per_speech)

    print('Entities statistics:')
    print('--------------------')
    print('sum of unique entities of all speeches: ', sum_of_unique_entities_of_all_speeches)
    print('avg of unique entities per speech: ', average_unique_entities_per_speech)
    print('avg of unique entities per paragraph: ', avg_of_unique_entities_per_paragraph)