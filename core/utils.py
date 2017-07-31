import boto
import boto.s3
import boto.s3.connection
from boto.s3.connection import Key
from django.conf import settings


def get_conn(**kwargs):
    """Faz a conexão com o S3."""
    access_key_id = kwargs.get('access_key_id', settings.AWS_ACCESS_KEY_ID)
    secret_access_key = kwargs.get('secret_access_key',
                                   settings.AWS_SECRET_ACCESS_KEY)
    region = kwargs.get('region', settings.AWS_REGION)

    conn = boto.s3.connect_to_region(
        region,
        aws_access_key_id=access_key_id,
        aws_secret_access_key=secret_access_key,
        calling_format=boto.s3.connection.OrdinaryCallingFormat(),
    )
    return conn


def export_to_s3(filename, property_uuid, overwrite=False):
    """Envia arquivo para o S3.
    Args:
        overwrite (bool): sobrescreve caso exista uma key com o mesmo nome.
        pic (object): Instance of PropertyPics
    """
    try:
        conn = get_conn()
        bucket = conn.get_bucket(settings.AWS_STORAGE_BUCKET_NAME)

        k = Key(bucket)
        dest_name = '{path}/{filename}'.format(path=property_uuid,
                                               filename=filename)

        if dest_name:
            k.name = dest_name

        try:
            k.set_contents_from_filename(filename.name, replace=overwrite)
        except AttributeError:
            k.set_contents_from_filename(filename.filename, replace=overwrite)

        key_url = k.generate_url(expires_in=0, query_auth=False)
        key_url = key_url.replace('https', 'http')
        k.set_acl('public-read')
        return key_url
    except Exception as error:
        print(error)
        raise
