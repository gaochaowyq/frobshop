from oscar.apps.offer.views import OfferListView as CoreOfferListView

class OfferListView(CoreOfferListView):
    template_name = 'new_list.html'