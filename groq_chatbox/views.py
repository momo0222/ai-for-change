from django.shortcuts import render
from django.http import JsonResponse
from .groq_client import client
from accounts.models import StudentProfile
from django.utils.safestring import mark_safe
from openai import APIError, OpenAI
import pandas as pd
import numpy as np
from django.conf import settings

client = OpenAI(api_key=settings.OPENAI_API_KEY)

system_prompt = {
    "role": "system",
    "content": "You are an assistant. Offer scholarly advice to high school students."
}
chat_history = [system_prompt]

def school_chat(request):
    if request.user.is_authenticated:
        try:
            student_profile = StudentProfile.objects.get(user=request.user)

            # Pre-feed user profile data into chat history
            chat_history.append({"role": "system", "content": f"User's Name: {student_profile.first_name} {student_profile.last_name}"})
            chat_history.append({"role": "system", "content": f"Date of Birth: {student_profile.date_of_birth}"})
            chat_history.append({"role": "system", "content": f"Gender: {student_profile.get_gender_display()}"})
            chat_history.append({"role": "system", "content": f"Unweighted GPA: {student_profile.unweighted_gpa}"})
            chat_history.append({"role": "system", "content": f"Weighted GPA: {student_profile.weighted_gpa}"})
            chat_history.append({"role": "system", "content": f"SAT Score: {student_profile.sat_score}"})
            chat_history.append({"role": "system", "content": f"ACT Score: {student_profile.act_score}"})
            chat_history.append({"role": "system", "content": f"Address: {student_profile.address}, {student_profile.city}, {student_profile.state}, {student_profile.zipcode}"})
            chat_history.append({"role": "system", "content": f"Current School: {student_profile.current_school}"})
            chat_history.append({"role": "system", "content": f"Grade Level: {student_profile.grade_level}"})
            chat_history.append({"role": "system", "content": f"Courses Taken: {student_profile.courses_taken}"})
            chat_history.append({"role": "system", "content": f"Activities: {student_profile.activities}"})
            chat_history.append({"role": "system", "content": f"Awards: {student_profile.awards}"})
            chat_history.append({"role": "system", "content": f"Household Income: {student_profile.household_income}"})
            chat_history.append({"role": "system", "content": f"Parent Occupations: {student_profile.parent_occupations}"})
            chat_history.append({"role": "system", "content": f"Siblings Information: {student_profile.siblings_information}"})
            chat_history.append({"role": "system", "content": f"Interest/Major: {student_profile.interest_major}"})
            chat_history.append({"role": "system", "content": f"Trade School Preference: {student_profile.trade_school_preference}"})
            chat_history.append({"role": "system", "content": f"Career Aspirations: {student_profile.career_aspirations}"})
            chat_history.append({"role": "system", "content": f"Weekly Availability: {student_profile.weekly_availability}"})
            chat_history.append({"role": "system", "content": f"Time Commitments: {student_profile.time_commitments}"})
            chat_history.append({"role": "system", "content": f"Special Circumstances: {student_profile.special_circumstances}"})
            chat_history.append({"role": "system", "content": f"Languages Spoken: {student_profile.languages_spoken}"})
            chat_history.append({"role": "system", "content": f"Cultural Background: {student_profile.cultural_background}"})


        except StudentProfile.DoesNotExist:
            return JsonResponse({"error": "Student profile not found."})
        except Exception as e:
            return JsonResponse({"error": str(e)})
    if request.method == 'POST':
        user_input = request.POST.get('message')
        chat_history.append({"role": "user", "content": user_input})

        try:
            # response = client.chat.completions.create(
            #     model="llama3-70b-8192",
            #     messages=chat_history,
            #     max_tokens=1000,
            #     temperature=1.2
            # )
            # generated_response = response.choices[0].message.content
            completion = client.chat.completions.create(
                model='gpt-3.5-turbo',  # Adjust model name as needed
                messages=chat_history
            )

            # Append assistant's response from API to message_objects
            chat_history.append({
                'role': 'assistant',
                'content': completion.choices[0].message.content  # Assuming single choice response
            })
            # chat_history.append({"role": "assistant", "content": generated_response})
            return JsonResponse({"message": mark_safe(completion.choices[0].message.content)})
        except Exception as e:
            return JsonResponse({"error": str(e)})
    return render(request, 'groq_chatbox/chat.html')


def mentalhalth_chat(request):
    message_objects = []
    if request.method == 'POST':
        user_input = request.POST.get('message')
    
        message_objects.append({'role': 'assistant',
                            'content': 'You are a chatbot providing students and/or parents with a step-by-step plan to cope with mental health concerns.'})
        message_objects.append({'role': 'user', 'content': user_input})
    
        message_objects.append(
            {'role': 'assistant', 'content': 'I found 3 steps you should take to improve your mental health'})
        try:
            # Send messages to ChatGPT API for completion
            completion = client.chat.completions.create(
                model='gpt-3.5-turbo',  # Adjust model name as needed
                messages=message_objects
            )

            # Append assistant's response from API to message_objects
            message_objects.append({
                'role': 'assistant',
                'content': completion.choices[0].message.content  # Assuming single choice response
            })

            # Return the assistant's response to update the chat UI
            return JsonResponse({"message": mark_safe(completion.choices[0].message.content)})

        except Exception as e:
            return JsonResponse({"error": str(e)})

    

    return render(request, 'groq_chatbox/mental_health.html')

# def get_embedding(text, model="text-embedding-ada-002"):
#     text = text.replace("\n", " ")
#     return client.embeddings.create(input=[text], model=model).data[0].embedding

# def match_with_others(request):
#     if request.method == 'POST':
#         matches = []
#         profiles = StudentProfile.objects.all()

#         current_student = StudentProfile.objects.get(user=request.user)
#         profiles = profiles.exclude(id=current_student.id)

#         for profile in profiles:
#             mentor_info = {
#             'name': profile.first_name or '',  # Assuming User model has first_name and last_name fields
#             'job': profile.interest_major or profile.trade_school_preference or '',  # Adjust based on your logic
#             'location': profile.zipcode or '',  # Assuming zipcode is a field in StudentProfile
#             'day': profile.weekly_availability or '',  # Assuming weekly_availability is a field in StudentProfile
#             }
#             matches.append(mentor_info)
        
#         matches_df = pd.DataFrame(matches)
        

#         matches_df['combined'] = matches_df.apply(lambda row: f"{row['job']}, {row['location']}, {row['day']}, {row['name']}", axis=1)
#         matches_df['text_embedding'] = matches_df.combined.apply(lambda x: get_embedding(x, model='text-embedding-ada-002'))


#         student = StudentProfile.objects.get(user=request.user)
#         student_info = [
#             {'name': student.first_name+student.last_name, 'job': student.interest_major or profile.trade_school_preference or '', 'location': student.zipcode or '', 'day': student.weekly_availability or ''}
#         ]

        
#         students_df = pd.DataFrame(student_info)
        
#         students_df['combined'] = students_df.apply(lambda row: f"{row['job']}, {row['location']}, {row['day']}, {row['name']}", axis=1)
#         students_df['text_embedding'] = students_df.combined.apply(lambda x: get_embedding(x, model='text-embedding-ada-002'))


#         students_input = "Recommend a mentor for me."
#         answer = client.embeddings.create(input=students_input, model='text-embedding-ada-002')

#         embedding_student_question = answer.data[0].embedding

#         embedding_student_question_vec = np.array(embedding_student_question).reshape(1, -1)


#         message_objects = []
#         message_objects.append({'role': 'system',
#                             'content': 'You are a chatbot providing students with mentor recommendations'})
#         message_objects.append({'role': 'user', 'content': students_input})
#         message_objects.append({'role': 'user',
#                             'content': 'Please give me a description of your recommendations'})
#         message_objects.append({'role': 'user', 'content': ''})
#         message_objects.append({'role': 'assistant', 'content': 'I found 2 mentors I would recommend'})

#         mentor_list = []

#         for index, row in matches_df.head(2).iterrows():
#             mentor_dict = {'role': 'assistant', 'content': f"{row['combined']}"}
#             mentor_list.append(mentor_dict)

#         message_objects.extend(mentor_list)
#         message_objects.append({'role': 'assistant',
#                             'content': 'Here is my summarized recommendation of mentors, and why they would suit you:'})
#         try:
#             completion = client.chat.completions.create(model='gpt-3.5-turbo',
#             messages=message_objects)

#             # Return the assistant's response to update the chat UI
#             print(completion.choices[0].message.content)
#             return JsonResponse({"message": mark_safe(completion.choices[0].message.content)})

#         except Exception as e:
#             return JsonResponse({"error": str(e)})
#     return render(request, 'groq_chatbox/matches.html')
    
def match_with_others(request):
    if request.method == 'POST':
        matches = []
        profiles = StudentProfile.objects.all()

        current_student = StudentProfile.objects.get(user=request.user)
        profiles = profiles.exclude(id=current_student.id)

        for profile in profiles:
            mentor_info = {
                'name': (profile.first_name or '') + ' ' + (profile.last_name or ''),  # Assuming User model has first_name and last_name fields
                'job': profile.interest_major or profile.trade_school_preference or '',  # Adjust based on your logic
                'location': profile.zipcode or '',  # Assuming zipcode is a field in StudentProfile
                'day': profile.weekly_availability or '',  # Assuming weekly_availability is a field in StudentProfile
            }
            matches.append(mentor_info)

        # Prepare the student info
        student_info = {
            'name': current_student.first_name + ' ' + current_student.last_name or '',
            'job': current_student.interest_major or current_student.trade_school_preference or '',
            'location': current_student.zipcode or '',
            'day': current_student.weekly_availability or ''
        }

        # Prepare the message for GPT
        students_input = "Recommend a mentor for me."
        message_objects = [
            {'role': 'system', 'content': 'You are a chatbot providing students with mentor recommendations'},
            {'role': 'user', 'content': f"My profile: {student_info}"},
            {'role': 'user', 'content': 'Here is the list of available mentors/peers:'},
            {'role': 'user', 'content': f"{matches}"},
            {'role': 'user', 'content': 'Please recommend two mentors/fellow students that would best match my profile.'}
        ]

        try:
            completion = client.chat.completions.create(model='gpt-3.5-turbo', messages=message_objects)

            # Return the assistant's response to update the chat UI
            return JsonResponse({"message": mark_safe(completion.choices[0].message.content)})

        except Exception as e:
            return JsonResponse({"error": str(e)})

    return render(request, 'groq_chatbox/matches.html')
