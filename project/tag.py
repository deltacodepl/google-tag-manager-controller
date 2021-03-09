from pprint import pprint


class Tag:
    def __init__(self, workspaces):

        if workspaces:
            self.tags = workspaces.tags()
        else:
            print("workspaces not exist")

    def create_html_tag(self, workspace_path, tag_info):

        tag = {
            "name": tag_info["tag_name"],
            "type": tag_info["tag_type"],
            "parameter": [
                {"key": "html", "type": "template", "value": tag_info["script"]}
            ],
        }

        try:
            self.tags.create(parent=workspace_path, body=tag).execute()
            print(" 🎉 TAG Created🎉")
            return self.tags
        except:
            print("💣 TAG not Created 💣")

    def create_ga_pageview(self, workspace_path, tag_info):

        tag = {
            "name": tag_info["tag_name"],
            "type": "ua",
            "parameter": [
                {
                    "key": "trackingId",
                    "type": "template",
                    "value": str(tag_info["ua_id"]),
                }
            ],
        }

        try:
            self.tags.create(parent=workspace_path, body=tag).execute()
            print(" 🎉 TAG Created🎉")
            return self.tags
        except:
            print("💣 TAG not Created 💣")

    def create_ga_event(self, workspace_path, tag_info):

        tag = {
            "name": tag_info["tag_name"],
            "type": "ua",
            "parameter": [
                {
                    "key": "gaSettings",
                    "type": "template",
                    "value": tag_info["ga_settings"],
                },
                {
                    "key": "nonInteraction",
                    "type": "boolean",
                    "value": tag_info["non_interaction"],
                },
                {"key": "trackType", "type": "template", "value": "TRACK_EVENT"},
                {
                    "key": "eventCategory",
                    "type": "template",
                    "value": tag_info["event_category"],
                },
                {
                    "key": "eventAction",
                    "type": "template",
                    "value": tag_info["event_action"],
                },
                {
                    "key": "eventLabel",
                    "type": "template",
                    "value": tag_info["event_label"],
                },
            ],
        }

        try:
            self.tags.create(parent=workspace_path, body=tag).execute()
            print(" 🎉 TAG Created🎉")
            return self.tags
        except:
            print("💣 TAG not Created 💣")

    def create_gads(self, workspace_path, tag_info):

        tag = {
            "name": tag_info["tag_name"],
            "type": tag_info["tag_type"],
            "parameter": [
                {
                    "key": "conversionId",
                    "type": "template",
                    "value": tag_info["conv_id"],
                },
                {
                    "key": "conversionLabel",
                    "type": "template",
                    "value": tag_info["conv_label"],
                },
            ],
        }

        try:
            self.tags.create(parent=workspace_path, body=tag).execute()
            print(" 🎉 TAG Created🎉")
            return self.tags
        except:
            print("💣 TAG not Created 💣")

    def create_flc(self, workspace_path, tag_info):

        tag = {
            "name": tag_info["tag_name"],
            "type": tag_info["tag_type"],
            "parameter": [
                {
                    "key": "advertiserId",
                    "type": "template",
                    "value": tag_info["advertiser_id"],
                },
                {"key": "groupTag", "type": "template", "value": tag_info["group_tag"]},
                {
                    "key": "activityTag",
                    "type": "template",
                    "value": tag_info["activity_tag"],
                },
                {
                    "key": "ordinalType",
                    "type": "template",
                    "value": tag_info["count_method"],
                },
            ],
        }

        try:
            self.tags.create(parent=workspace_path, body=tag).execute()
            print(" 🎉 TAG Created🎉")
            return self.tags
        except:
            print("💣 TAG not Created 💣")

    def create_fls(self, workspace_path, tag_info):

        tag = {
            "name": tag_info["tag_name"],
            "type": tag_info["tag_type"],
            "parameter": [
                {
                    "key": "advertiserId",
                    "type": "template",
                    "value": tag_info["advertiser_id"],
                },
                {"key": "groupTag", "type": "template", "value": tag_info["group_tag"]},
                {
                    "key": "activityTag",
                    "type": "template",
                    "value": tag_info["activity_tag"],
                },
                {
                    "key": "ordinalType",
                    "type": "template",
                    "value": tag_info["count_method"],
                },
                {"key": "orderId", "type": "template", "value": tag_info["order_id"]},
                {"key": "revenue", "type": "template", "value": tag_info["revenue"]},
            ],
        }

        try:
            self.tags.create(parent=workspace_path, body=tag).execute()
            print(" 🎉 TAG Created 🎉")
            return self.tags
        except:
            print("💣 TAG not Created 💣")

    def get_tag_by_name(self, workspace_path, tag_name):
        tags = self.tags.list(parent=workspace_path).execute()

        for tag in tags["tag"]:
            if tag["name"] == tag_name:
                return tag

        return None

    def connect_tag_trigger(self, tag, trigger):
        tag = self.tags.get(path=tag["path"]).execute()
        tag["firingTriggerId"] = [trigger["triggerId"]]
        response = self.tags.update(path=tag["path"], body=tag).execute()

    def tag_info(self, tag):
        pprint(tag)
