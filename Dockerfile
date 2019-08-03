FROM python:slim
LABEL maintainer "Setuu <setuu@neigepluie.net>"

RUN rm /etc/localtime && \
    ln -s /usr/share/zoneinfo/Asia/Tokyo /etc/localtime

RUN pip3 install requests
COPY reminder.py /reminder.py

CMD ["python3", "reminder.py"]
