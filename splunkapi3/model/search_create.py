from splunkapi3.model.model import Model


class SearchCreate(Model):

    name_map = {
        'id_': 'id',
        'indexed_realtime': 'indexedRealtime',
        'indexed_realtime_offset': 'indexedRealtimeOffset'
    }

    def __init__(self, auto_cancel: int = None, auto_finalize_ec: int = None,
                 auto_pause: int = None, custom: str = None, earliest_time: str = None,
                 enable_lookups: bool = None, exec_mode: str = None,
                 force_bundle_replication=None,
                 id_=None,
                 index_earliest=None,
                 index_latest=None,
                 indexed_realtime=None,
                 indexed_realtime_offset=None,
                 latest_time=None,
                 max_count=None,
                 max_time=None,
                 namespace=None,
                 now=None,
                 reduce_freq=None,
                 reload_macros=None,
                 remote_server_list=None,
                 replay_speed=None,
                 replay_et=None,
                 replay_lt=None,
                 required_field_list=None,
                 reuse_max_seconds_ago=None,
                 rf=None,
                 rt_blocking=None,
                 rt_indexfilter=None,
                 rt_maxblocksecs=None,
                 rt_queue_size=None,
                 search=None,
                 required=None,
                 search_listener=None,
                 search_mode=None,
                 spawn_process=None,
                 status_buckets=None,
                 sync_bundle_replication=None,
                 time_format=None,
                 timeout=None
                 ):
        """
        :param auto_cancel: If specified, the job automatically cancels after this many
        seconds of inactivity. (0 means never auto-cancel)

        :param auto_finalize_ec: Auto-finalize the search after at least this many events
        are processed. Specify 0 to indicate no limit.

        :param auto_pause: If specified, the search job pauses after this many seconds of
        inactivity. (0 means never auto-pause.)

        :param custom: Specify a custom parameter (see example).

        :param earliest_time: Specify a time string. Sets the earliest (inclusive),
        respectively, time bounds for the search.
        The time string can be either a UTC time (with fractional seconds), a relative
        time specifier (to now) or a formatted time string. Refer to Time modifiers for
        search for information and examples of specifying a time string.

        :param enable_lookups: Indicates whether lookups should be applied to events.
        Specifying true (the default) may slow searches significantly depending on the
        nature of the lookups.

        :param exec_mode: Valid values: (blocking | oneshot | normal)
        If set to normal, runs an asynchronous search.
        If set to blocking, returns the sid when the job is complete.
        If set to oneshot, returns results in the same call. In this case, you can specify
        the format for the output (for example, json output) using the output_mode
        parameter as described in GET search/jobs/export. Default format for output is xml.

        :param force_bundle_replication: Specifies whether this search should cause
        (and wait depending on the value of sync_bundle_replication) for bundle
        synchronization with all search peers.

        :param id_: Optional string to specify the search ID (<sid>). If unspecified,
        a random ID is generated.

        :param index_earliest:
        :param index_latest:
        :param indexed_realtime:
        :param indexed_realtime_offset:
        :param latest_time:
        :param max_count:
        :param max_time:
        :param namespace:
        :param now:
        :param reduce_freq:
        :param reload_macros:
        :param remote_server_list:
        :param replay_speed:
        :param replay_et:
        :param replay_lt:
        :param required_field_list:
        :param reuse_max_seconds_ago:
        :param rf:
        :param rt_blocking:
        :param rt_indexfilter:
        :param rt_maxblocksecs:
        :param rt_queue_size:
        :param search:
        :param required:
        :param search_listener:
        :param search_mode:
        :param spawn_process:
        :param status_buckets:
        :param sync_bundle_replication:
        :param time_format:
        :param timeout:
        """
        self.auto_cancel = auto_cancel
        self.auto_finalize_ec = auto_finalize_ec
        self.auto_pause = auto_pause
        self.custom = custom
        self.earliest_time = earliest_time
        self.enable_lookups = enable_lookups
        self.exec_mode = exec_mode
        self.force_bundle_replication = force_bundle_replication
        self.id_ = id_
        self.index_earliest = index_earliest
        self.index_latest = index_latest
        self.indexed_realtime = indexed_realtime
        self.indexed_realtime_offset = indexed_realtime_offset
        self.latest_time = latest_time
        self.max_count = max_count
        self.max_time = max_time
        self.namespace = namespace
        self.now = now
        self.reduce_freq = reduce_freq
        self.reload_macros = reload_macros
        self.remote_server_list = remote_server_list
        self.replay_speed = replay_speed
        self.replay_et = replay_et
        self.replay_lt = replay_lt
        self.required_field_list = required_field_list
        self.reuse_max_seconds_ago = reuse_max_seconds_ago
        self.rf = rf
        self.rt_blocking = rt_blocking
        self.rt_indexfilter = rt_indexfilter
        self.rt_maxblocksecs = rt_maxblocksecs
        self.rt_queue_size = rt_queue_size
        self.search = search
        self.required = required
        self.search_listener = search_listener
        self.search_mode = search_mode
        self.spawn_process = spawn_process
        self.status_buckets = status_buckets
        self.sync_bundle_replication = sync_bundle_replication
        self.time_format = time_format
        self.timeout = timeout
