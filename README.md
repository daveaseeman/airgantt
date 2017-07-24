# Task Gantt

df = [dict(Task="Job-1", Start='2017-01-01', Finish='2017-02-02', Resource='Complete'),
      dict(Task="Job-1", Start='2017-02-15', Finish='2017-03-15', Resource='Incomplete'),
      dict(Task="Job-2", Start='2017-01-17', Finish='2017-02-17', Resource='Not Started'),
      dict(Task="Job-2", Start='2017-01-17', Finish='2017-02-17', Resource='Complete'),
      dict(Task="Job-3", Start='2017-03-10', Finish='2017-03-20', Resource='Not Started'),
      dict(Task="Job-3", Start='2017-04-01', Finish='2017-04-20', Resource='Not Started'),
      dict(Task="Job-3", Start='2017-05-18', Finish='2017-06-18', Resource='Not Started'),
      dict(Task="Job-4", Start='2017-01-14', Finish='2017-03-14', Resource='Complete')]

colors = {'Not Started': 'rgb(220, 0, 0)',
          'Incomplete': (1, 0.9, 0.16),
          'Complete': 'rgb(0, 255, 100)'}

records is a list
each list item is an ordered dictionary
the key 'fields' has an ordered dictionary value
the key 'Project' has a list value
the key 'Assignee' has an ordered dictionary value


[(u'id', u'recM2eNtXCnYB5vjc'),
 (u'fields', OrderedDict([(u'Start', u'2017-06-01'),
                          (u'Status', u'to-do'),
                          (u'Finish', u'2017-06-08'),
                          (u'Project', [u'recCGw1O9KrDRbunk']),
                          (u'Task Name', u'ID'),
                          (u'Assignee', OrderedDict([(u'id', u'usrqFy1ZealR6LCi5'),
                                                     (u'email', u'evan@fractalhardware.com'),
                                                     (u'name', u'Evan Reese')])
                           )])),
 (u'createdTime', u'2017-06-14T17:07:16.000Z')]

 [OrderedDict([(u'id', u'recCGw1O9KrDRbunk'),
               (u'fields', OrderedDict([(u'Name', u'Mio Caffe Affare'),
                                        (u'Tasks', [u'recM2eNtXCnYB5vjc']),
                                        (u'Person', u'Dave'),
                                        (u'Scope', [OrderedDict([(u'id', u'atttXebrcrWoGh83B'),
                                                                 (u'url', u'https://dl.airtable.com/soAAGymT6aVSMAd3Mkf6_Project%20Proposal%20-%20Mio%20Caffe%20Affare.pdf'),
                                                                 (u'filename', u'Project Proposal - Mio Caffe Affare.pdf'),
                                                                 (u'size', 30032),
                                                                 (u'type', u'application/pdf'),
                                                                 (u'thumbnails', OrderedDict([(u'small', OrderedDict([(u'url', u'https://dl.airtable.com/atttXebrcrWoGh83B-28x36.png'),
                                                                                                                      (u'width', 28),
                                                                                                                      (u'height', 36)])),
                                                                                              (u'large', OrderedDict([(u'url', u'https://dl.airtable.com/atttXebrcrWoGh83B-512x663.png'),
                                                                                                                      (u'width', 512),
                                                                                                                      (u'height', 663)]))]))])])])),
               (u'createdTime', u'2017-06-14T16:33:35.000Z')]),
  OrderedDict([(u'id', u'recCZpsWQjWoHg7NN'),
               (u'fields', OrderedDict([(u'Person', u'Dave')])),
               (u'createdTime', u'2017-06-14T17:01:56.000Z')]), OrderedDict([(u'id', u'recPnTW7FNb1zEwbA'),
                                                                             (u'fields', OrderedDict([(u'Status', u'Current'),
                                                                                                      (u'Name', u'Dynamic Magnetics'),
                                                                                                      (u'Tasks', [
                                                                                                       u'recSC6Ro8rkUCTCGl', u'recuZDaSX6M4a4gv2', u'recuNPEK1Emc2RsOC']),
                                                                                                      (u'Person', u'Dave'),
                                                                                                      (u'Target Date', u'2017-09-08'),
                                                                                                      (u'Scope', [OrderedDict([(u'id', u'attzRpPRHrAcQZK5e'),
                                                                                                                               (u'url', u'https://dl.airtable.com/KAJ3HHfPS0C6ZjloDoLV_Project%20Proposal%20-%20Dynamic%20Magnetics%20V3.1.pdf'),
                                                                                                                               (u'filename', u'Project Proposal - Dynamic Magnetics V3.1.pdf'),
                                                                                                                               (u'size', 35858), (u'type',
                                                                                                                                                  u'application/pdf'),
                                                                                                                               (u'thumbnails', OrderedDict([(u'small', OrderedDict([(u'url', u'https://dl.airtable.com/attzRpPRHrAcQZK5e-28x36.png'),
                                                                                                                                                                                    (u'width', 28), (u'height', 36)])),
                                                                                                                                                            (u'large', OrderedDict([(u'url', u'https://dl.airtable.com/attzRpPRHrAcQZK5e-512x663.png'),
                                                                                                                                                                                    (u'width', 512),
                                                                                                                                                                                    (u'height', 663)]))]))])])])), (u'createdTime', u'2017-06-04T17:29:19.000Z')]), OrderedDict([(u'id', u'recbkDkmygt39MLG0'), (u'fields', OrderedDict([(u'Status', u'Current'), (u'Name', u'WeighUP'), (u'Person', u'Mitch'), (u'Target Date', u'2017-07-24'), (u'Scope', [OrderedDict([(u'id', u'attdrEUzIwrpsbclq'), (u'url', u'https://dl.airtable.com/VHmxd1u4QnqNZXIA2f3T_Project%20Proposal%20-%20WeighUp%20V2.pdf'), (u'filename', u'Project Proposal - WeighUp V2.pdf'), (u'size', 60319), (u'type', u'application/pdf'), (u'thumbnails', OrderedDict([(u'small', OrderedDict([(u'url', u'https://dl.airtable.com/attdrEUzIwrpsbclq-28x36.png'), (u'width', 28), (u'height', 36)])), (u'large', OrderedDict([(u'url', u'https://dl.airtable.com/attdrEUzIwrpsbclq-512x663.png'), (u'width', 512), (u'height', 663)]))]))])]), (u'Harvest', u'https://fractalhardware.harvestapp.com/projects/14206365'), (u'Drive', u'https://drive.google.com/drive/folders/0Bw6dslFqckFeVTgyUWRwZFBVQnM')])), (u'createdTime', u'2017-06-14T16:59:17.000Z')]), OrderedDict([(u'id', u'rechmXwWDrkilV9hj'), (u'fields', OrderedDict([(u'Status', u'Current'), (u'Name', u'Glove Last'), (u'Person', u'Evan')])), (u'createdTime', u'2017-06-04T17:29:19.000Z')])]
# airgantt
