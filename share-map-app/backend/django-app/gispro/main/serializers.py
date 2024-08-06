from rest_framework import serializers
from .models import ActionButton, PositionView,\
    Map, Location, Drawing, Category, Marker


class DrawingSerializer(serializers.ModelSerializer):
    class Meta:
        model = Drawing
        fields = '__all__'


class MarkerSerializer(serializers.ModelSerializer):
    class Meta:
        model = Marker
        fields = '__all__'


class ActionBtnSerializer(serializers.ModelSerializer):
    class Meta:
        model = ActionButton
        fields = '__all__'


class PositionViewSerializer(serializers.ModelSerializer):
    class Meta:
        model = PositionView
        fields = '__all__'


class CategorySerializer(serializers.ModelSerializer):
    marker = MarkerSerializer(many=False)

    class Meta:
        model = Category
        fields = '__all__'

    def create(self, validated_data):
        marker_data = validated_data.pop('marker')
        drawing_data = validated_data.pop('drawing')
        marker = Marker.objects.create(**marker_data)
        marker.save()

        category = Category.objects.create(marker=marker, **validated_data)

        for draw in drawing_data:
            category.drawing.add(draw)

        category.save()
        return category

    def update(self, instance, validated_data):
        drawing_data = validated_data.pop('drawing')
        marker_data = validated_data.pop('marker')

        instance.name = validated_data.get('name', instance.name)
        instance.marker.marker_type = marker_data.get('marker_type', instance.marker.marker_type)
        instance.marker.size = marker_data.get('size', instance.marker.size)
        instance.marker.image = marker_data.get('image', instance.marker.image)
        instance.marker.color = marker_data.get('color', instance.marker.color)
        instance.marker.marker_text = marker_data.get('marker_text', instance.marker.marker_text)
        instance.marker.text_size = marker_data.get('text_size', instance.marker.text_size)

        instance.marker.save()
        instance.drawing.clear()

        for draw in drawing_data:
            instance.drawing.add(draw)

        instance.save()
        return instance


class MapSerializer(serializers.ModelSerializer):
    action_btn = ActionBtnSerializer(many=False)

    class Meta:
        model = Map
        fields = '__all__'

    def create(self, validated_data):
        action_btn_data = validated_data.pop('action_btn')
        drawing_data = validated_data.pop('drawing')
        action_btn = ActionButton.objects.create(**action_btn_data)
        action_btn.save()

        map = Map.objects.create(action_btn=action_btn, **validated_data)

        for draw in drawing_data:
            map.drawing.add(draw)

        map.save()
        return map

    def update(self, instance, validated_data):
        action_btn_data = validated_data.pop('action_btn')
        drawing_data = validated_data.pop('drawing')

        instance.title = validated_data.get('title', instance.title)
        instance.desc = validated_data.get('desc', instance.desc)
        instance.logo = validated_data.get('logo', instance.logo)
        instance.status = validated_data.get('status', instance.status)
        instance.action_btn.url = action_btn_data.get('url', instance.action_btn.url)
        instance.action_btn.btn_title = action_btn_data.get('btn_title', instance.action_btn.btn_title)
        instance.action_btn.open_link_in = action_btn_data.get('open_link_in', instance.action_btn.open_link_in)
        instance.action_btn.save()


        instance.drawing.clear()

        for draw in drawing_data:
            instance.drawing.add(draw)

        instance.save()
        return instance



class LocationSerializer(serializers.ModelSerializer):

    action_btn = ActionBtnSerializer(many=False)
    marker = MarkerSerializer(many=False)
    position_view = PositionViewSerializer(many=False)

    class Meta:
        model = Location
        fields = '__all__'

    def create(self, validated_data):
        action_btn_data = validated_data.pop('action_btn')
        marker_data = validated_data.pop('marker')
        position_data = validated_data.pop('position_view')

        drawing_data = validated_data.pop('drawing')
        category_data = validated_data.pop('category')

        action_btn = ActionButton.objects.create(**action_btn_data)
        marker = Marker.objects.create(**marker_data)
        position = PositionView.objects.create(**position_data)
        action_btn.save()
        marker.save()
        position.save()

        location = Location.objects.create(action_btn = action_btn,
                                           marker = marker,
                                           position_view = position,
                                           **validated_data)

        for draw in drawing_data:
            location.drawing.add(draw)

        for category in category_data:
            location.drawing.add(category)


        location.save()
        return location


