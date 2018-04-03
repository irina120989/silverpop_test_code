''' test svp api calls'''
from silverpop_test import Engage
from silverpop_test import EngageResponse

api_url = 'http://api3.ibmmarketingcloud.com/XMLAPI'
ftp_url = '74.121.50.5'

eng = Engage(api_url, ftp_url)

resp = eng.login(username='', password='')
eng.ftp_address = 'transfer3.silverpop.com'

xml_purge_contact = '''
<Envelope>
	<Body>
		<RawRecipientDataExport>
			<EVENT_DATE_START>03/28/2018 09:25:00</EVENT_DATE_START>
			<EVENT_DATE_END>03/29/2018 09:30:59</EVENT_DATE_END>
            <MOVE_TO_FTP/>
			<EXPORT_FORMAT>0</EXPORT_FORMAT>
			<EXCLUDE_DELETED/>
			<EMAIL> </EMAIL>
			<ALL_EVENT_TYPES/>
			<INCLUDE_INBOX_MONITORING/>
			<RETURN_MAILING_NAME/>
			<RETURN_SUBJECT/>
			<COLUMNS>
				<COLUMN>
					<NAME>CustomerID</NAME>
				</COLUMN>
				<COLUMN>
					<NAME>First Name</NAME>
				</COLUMN>
				<COLUMN>
					<NAME>Last Name</NAME>
				</COLUMN>
			</COLUMNS>
		</RawRecipientDataExport>
	</Body>
</Envelope>
'''

resp = eng.xml_engage_request(xml_purge_contact)
# if resp.SUCCESS : print('success')
handle_job(EngageResponse)
# get_file = eng.ftp_getfile(
# 'Raw Recipient Data Export Apr 01 2018 05-19-00 AM 1994.zip',
# '/Users/irinabarbu/Documents/silverpoppy_test.zip')

