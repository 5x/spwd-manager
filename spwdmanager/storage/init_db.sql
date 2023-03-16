CREATE TABLE IF NOT EXISTS  records (
	record_id INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT,
	title BLOB,
	category BLOB DEFAULT 'default' NOT NULL,
	salt BLOB,
	json BLOB,
	created_at INTEGER DEFAULT CURRENT_TIMESTAMP NOT NULL,
	updated_at INTEGER DEFAULT CURRENT_TIMESTAMP NOT NULL
);

CREATE UNIQUE INDEX IF NOT EXISTS records_id_IDX ON records (record_id);

CREATE TABLE IF NOT EXISTS  settings (
    name TEXT NOT NULL PRIMARY KEY,
    data  TEXT DEFAULT NULL
);

INSERT OR REPLACE INTO settings (name, data) VALUES
  ('store_salt', '{{UNIQUE_STORE_SALT}}'),
  ('store_token', '{{spwd-manager}}'),
  ('group_by_category', TRUE),
  ('sort_by', 'title'),
  ('sort_revers', FALSE),
  ('theme', 'litera'),
  ('language', 'en');
