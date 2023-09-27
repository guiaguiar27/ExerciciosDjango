#!/bin/bash

DB_USER="Django_user"
DB_PASSWORD="123password"
DB_NAME="database"


BACKUP_DIR="~/desktop/work/test/"
TIMESTAMP=$(date +"%Y%m%d%H%M%S")
BACKUP_FILE="$BACKUP_DIR/$DB_NAME-backup-$TIMESTAMP.sql"


mysqldump -u "$DB_USER" -p"$DB_PASSWORD" "$DB_NAME" > "$BACKUP_FILE"


if [ $? -eq 0 ]; then
  echo "Backup completed successfully. Backup file: $BACKUP_FILE"
else
  echo "Backup failed."
fi
